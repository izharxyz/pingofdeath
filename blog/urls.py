from django.urls import path
from .views import BlogView, BlogHomeView, SingleBlogView

urlpatterns = [
    path('', BlogView.as_view()), # returns random list of blogs for all users
    path('home/', BlogHomeView.as_view()), # return blogs of authenticated user, hence blog can be created, updated and deleted
    path('<slug:pk>', SingleBlogView.as_view()) # absolute url for getting a single blog, pk is blog uid
]
