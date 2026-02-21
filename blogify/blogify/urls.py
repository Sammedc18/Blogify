from django.contrib import admin
from django.urls import include, path
from Blogapp.views import *
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('category/',include('Blogapp.urls')),
    path('blog/<slug:slug>/',blogs,name='blogs'),
    # search endpoint
    path('blogs/search/',search,name='search'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)