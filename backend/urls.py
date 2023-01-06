from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('authapi.urls')),
    path('blog/', include('blog.urls'))
]

urlpatterns += staticfiles_urlpatterns()