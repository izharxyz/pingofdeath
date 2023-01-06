from django.urls import path
from .views import BlogView, BlogHomeView, SingleBlogView

urlpatterns = [
    path('', BlogView.as_view()),
    path('home/', BlogHomeView.as_view()),
    path('<slug:pk>', SingleBlogView.as_view())
]
