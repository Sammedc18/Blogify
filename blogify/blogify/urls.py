from django.contrib import admin
from django.urls import include, path
from Blogapp.views import home
from django.conf.urls.static import static
from django.conf import settings
from Blogapp import views as BlogsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('category/', include('Blogapp.urls')),  
    path('<slug:slug>/', BlogsView.blogs, name='blogs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
