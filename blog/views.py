from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator
import jwt

from .serializers import BlogSerializer
from .models import Blog

class BlogHomeView(APIView):
    def get(self, request):
        try:
            blog = Blog.objects.all().order_by('?') # fetch random blogs for home page

            if request.GET.get('search'):
                search = request.GET.get('search')
                blog = blog.filter(Q(title__icontains = search) | Q(body__icontains = search))
            
            page_number = request.GET.get('page', 1)
            paginator = Paginator(blog, 9)

            serializer = BlogSerializer(paginator.page(page_number), many=True)
            return Response({
                'detail': serializer.data,
                'message': 'blog fetched successfully'
            })

        except:
            return Response({
                'detail': {},
                'message': 'something went wrong'
            })


class BlogView(APIView):

    # the deafult home page
    def get(self, request):
        token = request.COOKIES.get('token')
        
        if not token:
            raise AuthenticationFailed('unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', ['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('unauthenticated')

        # home page will return only user's own post if user is logged in
        user = User.objects.filter(id = payload['id']).first()

        try:
            blog = Blog.objects.filter(owner=user.id)

            if request.GET.get('search'):
                search = request.GET.get('search')
                blog = blog.filter(Q(title__icontains = search) | Q(body__icontains = search))

            serializer = BlogSerializer(blog, many=True)
            return Response({
                'detail': serializer.data,
                'message': 'blog fetched successfully'
            })
        # if user is not logged in
        except:
            return Response({
                'detail': {},
                'message': 'something went wrong'
            })


    # post method to create blog
    def post(self, request): 
        token = request.COOKIES.get('token')
        
        if not token:
            raise AuthenticationFailed('unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', ['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('unauthenticated')

        user = User.objects.filter(id = payload['id']).first()

        if user.is_authenticated:
            data = request.data
            data['owner'] = user.id
            serializer = BlogSerializer(data = data)
            if not serializer.is_valid():
                return Response({
                    'detail': serializer.errors,
                    'message': 'something went wrong'
                })
            
            serializer.save()

            return Response({
                'detail': serializer.data,
                'message': 'blog created successfully'
            }, status=status.HTTP_201_CREATED)


    def patch(self, request): 
        token = request.COOKIES.get('token')
        
        if not token:
            raise AuthenticationFailed('unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', ['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('unauthenticated')

        user = User.objects.filter(id = payload['id']).first()

        if user.is_authenticated:
            data = request.data

            try:
                blog = Blog.objects.filter(uid = data.get('uid')).first()
                _ = blog.title # will fail if blog = None
            except:
                return Response({
                    'detail': {},
                    'message': 'invalid blog uid'
                })
            
            if user == blog.owner:
                serializer = BlogSerializer(blog, data=data, partial=True)

                if not serializer.is_valid():
                    return Response({
                        'detail': serializer.errors,
                        'message': 'something went wrong'
                    })

                serializer.save()

                return Response({
                    'detail': serializer.data,
                    'message': 'blog updated successfully'
                })
            else:
                return Response({
                    'detail': {},
                    'message': 'operation not permitted'
                })
        
    def delete(self, request): 
        token = request.COOKIES.get('token')
        
        if not token:
            raise AuthenticationFailed('unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', ['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('unauthenticated')

        user = User.objects.filter(id = payload['id']).first()

        if user.is_authenticated:
            data = request.data

            try:
                blog = Blog.objects.filter(uid = data.get('uid')).first()
                _ = blog.title # will fail if blog = None
            except:
                return Response({
                    'detail': {},
                    'message': 'invalid blog uid'
                })
            
            if user == blog.owner:
                blog.delete()
                return Response({
                    'detail': {},
                    'message': 'blog updated successfully'
                })
            else:
                return Response({
                    'detail': {},
                    'message': 'operation not permitted'
                })
    
class SingleBlogView(APIView):
    def get(self, request, pk):
        
        try:
            blog = Blog.objects.filter(uid = pk).first()
            serializer = BlogSerializer(blog)
            
            return Response({
                'detail': serializer.data,
                'message': 'blog fetched successfully'
            })
        except:
            return Response({
                'detail': {},
                'message': 'something went wrong'
            })