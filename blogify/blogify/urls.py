from django.contrib import admin
from django.urls import include, path
from Blogapp.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('category/',include('Blogapp.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)