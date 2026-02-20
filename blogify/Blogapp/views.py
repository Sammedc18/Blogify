from django.shortcuts import get_object_or_404, render

from Blogapp.models import Blog, Category



# Create your views here.

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True,).order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False)

    
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts':posts,
        }
    return render(request, 'home.html', context)


def posts_by_category(request,category_id):
    #fetch the posts that belongs to the category with the id category_id
    posts=Blog.objects.filter(status='Published', category=category_id)
    #use try or except when we want to do some custom action id the category does not exists
    #try:
     # category = Category.objects.get(pk=category_id)
    #except:
     # redirect the user to Homepage
    # return redirect('home')
    
    #use get_objext_or_404 when you want to show error page if the category does not exist
    category = get_object_or_404(Category,pk=category_id)

    context={
        'posts':posts,
       'category':category,
    }
    return render(request, 'posts_by_category.html', context)