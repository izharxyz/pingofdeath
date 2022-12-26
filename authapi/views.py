from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
import jwt, datetime 


class RegisterView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'detail': serializer.errors,
                    'message': 'something went wrong'
                }, status = status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response({
                'detail': {},
                'message': 'account created successfully!'
            }, status = status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response({
                'detail': {},
                'message': 'something went wrong'
            }, status = status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username = username).first()

        if user is None:
            raise AuthenticationFailed('user not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=3),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='token', value=token, httponly=True)
        response.data = {
            'detail': {},
            'message': 'login successful!'
        }

        return response


class HomeView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')
        
        if not token:
            raise AuthenticationFailed('unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', ['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('unauthenticated')

        user = User.objects.filter(id = payload['id']).first()
        return Response({
            'detail': {},
            'message': 'logged in'
        })

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('token')
        response.data = {
            'detail': {},
            'message': 'logged out successfully'
        }
        
        return response