from django.urls import include, path

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('api/accounts/', include('authapi.urls')),
    path('api/blog/', include('blog.urls'))
]
