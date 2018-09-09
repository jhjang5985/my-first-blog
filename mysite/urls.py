from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('blog.urls')),
]