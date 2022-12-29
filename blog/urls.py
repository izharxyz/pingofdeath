from django.urls import path
from .views import BlogView, BlogHomeView

urlpatterns = [
    path('', BlogView.as_view()),
    path('home/', BlogHomeView.as_view())
]
