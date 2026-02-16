from django.urls import path
from Blogapp.views import *

urlpatterns = [
    path('<int:category_id>/',posts_by_category,name='posts_by_category')
   
] 