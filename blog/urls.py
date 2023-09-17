from django.urls import path

from .views import (BlogCreateView, BlogDeleteView, BlogHomeView,
                    BlogUpdateView, BlogView, SingleBlogView)

urlpatterns = [
    # returns random list of blogs for all users
    path('', BlogView.as_view()),

    # return blogs of authenticated user
    path('home/', BlogHomeView.as_view()),

    # create a blog
    path('create/', BlogCreateView.as_view()),
    # update a blog
    path('update/', BlogUpdateView.as_view()),
    # delete a blog
    path('delete/', BlogDeleteView.as_view()),

    # absolute url for getting a single blog, pk is blog uid
    path('<slug:pk>', SingleBlogView.as_view())
]
