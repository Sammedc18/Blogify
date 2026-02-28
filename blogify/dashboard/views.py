# from django.shortcuts import get_object_or_404, redirect, render

# from Blogapp.models import Blog, Category
# from django.contrib.auth.decorators import login_required

# from .forms import  BlogPostForm, CategoryForm, EditUserForm
# from django.template.defaultfilters import slugify
# from django.contrib.auth.models import User
# from .forms import AddUserForm


# @login_required(login_url = 'login')
# def dashboard(request):
#     category_count = Category.objects.all().count()
#     blogs_count = Blog.objects.all().count()
    
#     context = {
#         "category_count" : category_count,
#         "blogs_count": blogs_count
#     }
#     return render(request, 'dashboard/dashboard.html', context)


# def categories(request):
#     return render(request, 'dashboard/categories.html')


# def add_category(request):
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('categories')
#     form = CategoryForm()
#     context = {
#         'form':form
#     }
#     return render(request, 'dashboard/add_category.html',context)

# def edit_category(request,pk):
#     category = get_object_or_404(Category, pk=pk)
#     if request.method == 'POST':
#         form = CategoryForm(request.POST, instance=category)
#         if form.is_valid():
#             form.save()
#             return redirect('categories')
#     form = CategoryForm(instance=category)
#     context = {
#         'form':form,
#         'category':category
#     }
#     return render(request, 'dashboard/edit_category.html',context)



# def delete_category(request,pk):
#     category = get_object_or_404(Category, pk=pk)
#     category.delete()
#     return redirect('categories') 


# def posts(request):
#     posts = Blog.objects.all()
#     context = {
#         'posts':posts,
#     }
#     return render(request,'dashboard/posts.html',context)


# def add_post(request):
#     if request.method == 'POST':
#      form = BlogPostForm(request.POST, request.FILES)
#      if form.is_valid():
#          post = form.save(commit=False) # temporarily saving the form
#          post.author = request.user
#          post.save()
#          title = form.cleaned_data['title']
#          post.slug = slugify(title) +'-'+str(post.id)
#          post.save()
#          return redirect('posts')
#      else:
#          print('form is invalid')
#          print(form.errors)
#     form = BlogPostForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'dashboard/add_post.html', context) 

# def edit_post(request, pk):
#     post = get_object_or_404(Blog, pk=pk)
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             title = form.cleaned_data['title']
#             post.slug = slugify(title) + '-'+str(post.id)
#             post.save()
#             return redirect('posts')
#     form = BlogPostForm(instance=post)
#     context = {
#         'form': form,
#         'post': post
#     }
#     return render(request, 'dashboard/edit_post.html',context)

# def delete_post(request, pk):
#     post = get_object_or_404(Blog, pk=pk)
#     post.delete()
#     return redirect('posts')

# def users(request):
#     users = User.objects.all()
#     context = {
#         'users':users,
#     }
#     return render(request,'dashboard/users.html', context)

# def add_user(request):
#     if request.method == "POST":
#         form = AddUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users')
#     else:
#         form = AddUserForm()

#     context = {
#         'form': form,
#     }
#     return render(request, 'dashboard/add_user.html', context)
# def edit_user(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     if request.method == 'POST':
#         form = EditUserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect ('users')
#     form = EditUserForm(instance=user)
#     context ={
#         'form': form,
#     }
#     return render(request, 'dashboard/edit_user.html', context) 
# def delete_user(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     user.delete()
#     return redirect('users')








# from django.shortcuts import get_object_or_404, redirect, render
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.auth.models import User
# from django.template.defaultfilters import slugify
# from django.http import HttpResponseForbidden

# from Blogapp.models import Blog, Category
# from .forms import BlogPostForm, CategoryForm, AddUserForm, EditUserForm


# # =========================
# # Helper: Staff Check
# # =========================
# def staff_required(view_func):
#     decorated_view_func = login_required(
#         user_passes_test(lambda u: u.is_staff)(view_func)
#     )
#     return decorated_view_func


# # =========================
# # Dashboard
# # =========================
# @login_required(login_url='login')
# def dashboard(request):
#     context = {
#         "category_count": Category.objects.count(),
#         "blogs_count": Blog.objects.count(),
#     }
#     return render(request, 'dashboard/dashboard.html', context)


# # =========================
# # Category Views (Staff Only)
# # =========================
# @login_required(login_url='login')
# def categories(request):
#     categories = Category.objects.all().order_by('-id')
#     return render(request, 'dashboard/categories.html', {'categories': categories})


# @staff_required
# def add_category(request):
#     form = CategoryForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('categories')

#     return render(request, 'dashboard/add_category.html', {'form': form})


# @staff_required
# def edit_category(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     form = CategoryForm(request.POST or None, instance=category)

#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('categories')

#     return render(request, 'dashboard/edit_category.html', {
#         'form': form,
#         'category': category
#     })


# @staff_required
# def delete_category(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     category.delete()
#     return redirect('categories')


# # =========================
# # Blog Post Views
# # =========================
# @login_required(login_url='login')
# def posts(request):
#     posts = Blog.objects.select_related('author', 'category').order_by('-created_at')
#     return render(request, 'dashboard/posts.html', {'posts': posts})


# # Any logged-in user can add post
# @login_required(login_url='login')
# def add_post(request):
#     form = BlogPostForm(request.POST or None, request.FILES or None)

#     if request.method == 'POST' and form.is_valid():
#         post = form.save(commit=False)
#         post.author = request.user
#         post.save()

#         post.slug = slugify(post.title) + "-" + str(post.id)
#         post.save()

#         return redirect('posts')

#     return render(request, 'dashboard/add_post.html', {'form': form})


# # Only staff OR author can edit
# @login_required(login_url='login')
# def edit_post(request, pk):
#     post = get_object_or_404(Blog, pk=pk)

#     if not (request.user.is_staff or request.user == post.author):
#         return HttpResponseForbidden("You are not allowed to edit this post.")

#     form = BlogPostForm(request.POST or None, request.FILES or None, instance=post)

#     if request.method == 'POST' and form.is_valid():
#         updated_post = form.save(commit=False)
#         updated_post.slug = slugify(updated_post.title) + "-" + str(updated_post.id)
#         updated_post.save()
#         return redirect('posts')

#     return render(request, 'dashboard/edit_post.html', {
#         'form': form,
#         'post': post
#     })


# # Only staff OR author can delete
# @login_required(login_url='login')
# def delete_post(request, pk):
#     post = get_object_or_404(Blog, pk=pk)

#     if not (request.user.is_staff or request.user == post.author):
#         return HttpResponseForbidden("You are not allowed to delete this post.")

#     post.delete()
#     return redirect('posts')


# # =========================
# # User Management (Staff Only)
# # =========================
# @staff_required
# def users(request):
#     users = User.objects.all().order_by('-date_joined')
#     return render(request, 'dashboard/users.html', {'users': users})


# @staff_required
# def add_user(request):
#     form = AddUserForm(request.POST or None)

#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('users')

#     return render(request, 'dashboard/add_user.html', {'form': form})


# @staff_required
# def edit_user(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     form = EditUserForm(request.POST or None, instance=user)

#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('users')

#     return render(request, 'dashboard/edit_user.html', {'form': form})


# @staff_required
# def delete_user(request, pk):
#     user = get_object_or_404(User, pk=pk)

#     if user.is_superuser:
#         return HttpResponseForbidden("Superuser cannot be deleted.")

#     user.delete()
#     return redirect('users')






# from django.shortcuts import get_object_or_404, redirect, render
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.auth.models import User
# from django.template.defaultfilters import slugify

# from Blogapp.models import Blog, Category
# from .forms import BlogPostForm, CategoryForm, EditUserForm, AddUserForm


# # =========================
# # Helper: Staff Check
# # =========================
# def staff_required(view_func):
#     return user_passes_test(
#         lambda u: u.is_staff,
#         login_url='login'
#     )(view_func)


# # =========================
# # Dashboard
# # =========================
# @login_required(login_url='login')
# def dashboard(request):
#     category_count = Category.objects.count()
#     blogs_count = Blog.objects.count()

#     context = {
#         "category_count": category_count,
#         "blogs_count": blogs_count
#     }
#     return render(request, 'dashboard/dashboard.html', context)


# # =========================
# # Category Management (Staff Only)
# # =========================
# @staff_required
# def categories(request):
#     categories = Category.objects.all()
#     return render(request, 'dashboard/categories.html', {'categories': categories})


# @staff_required
# def add_category(request):
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('categories')
#     else:
#         form = CategoryForm()

#     return render(request, 'dashboard/add_category.html', {'form': form})


# @staff_required
# def edit_category(request, pk):
#     category = get_object_or_404(Category, pk=pk)

#     if request.method == 'POST':
#         form = CategoryForm(request.POST, instance=category)
#         if form.is_valid():
#             form.save()
#             return redirect('categories')
#     else:
#         form = CategoryForm(instance=category)

#     return render(request, 'dashboard/edit_category.html', {
#         'form': form,
#         'category': category
#     })


# @staff_required
# def delete_category(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     category.delete()
#     return redirect('categories')


# # =========================
# # Posts
# # =========================
# @login_required(login_url='login')
# def posts(request):
#     posts = Blog.objects.all()
#     return render(request, 'dashboard/posts.html', {'posts': posts})


# @login_required(login_url='login')
# def add_post(request):
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()

#             post.slug = slugify(post.title) + '-' + str(post.id)
#             post.save()

#             return redirect('posts')
#     else:
#         form = BlogPostForm()

#     return render(request, 'dashboard/add_post.html', {'form': form})


# @login_required(login_url='login')
# def edit_post(request, pk):
#     post = get_object_or_404(Blog, pk=pk)

#     # Only Author or Staff can edit
#     if request.user != post.author and not request.user.is_staff:
#         return redirect('posts')

#     if request.method == 'POST':
#         form = BlogPostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             post.slug = slugify(post.title) + '-' + str(post.id)
#             post.save()
#             return redirect('posts')
#     else:
#         form = BlogPostForm(instance=post)

#     return render(request, 'dashboard/edit_post.html', {
#         'form': form,
#         'post': post
#     })


# @login_required(login_url='login')
# def delete_post(request, pk):
#     post = get_object_or_404(Blog, pk=pk)

#     # Only Author or Staff can delete
#     if request.user != post.author and not request.user.is_staff:
#         return redirect('posts')

#     post.delete()
#     return redirect('posts')


# # =========================
# # User Management (Staff Only)
# # =========================
# @staff_required
# def users(request):
#     users = User.objects.all()
#     return render(request, 'dashboard/users.html', {'users': users})


# @staff_required
# def add_user(request):
#     if request.method == "POST":
#         form = AddUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users')
#     else:
#         form = AddUserForm()

#     return render(request, 'dashboard/add_user.html', {'form': form})


# @staff_required
# def edit_user(request, pk):
#     user = get_object_or_404(User, pk=pk)

#     if request.method == 'POST':
#         form = EditUserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('users')
#     else:
#         form = EditUserForm(instance=user)

#     return render(request, 'dashboard/edit_user.html', {'form': form})


# @staff_required
# def delete_user(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     user.delete()
#     return redirect('users')





from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from Blogapp.models import Blog, Category
from .forms import BlogPostForm, CategoryForm, EditUserForm, AddUserForm


# =========================
# Helper: Staff Check
# =========================
def staff_required(view_func):
    return user_passes_test(
        lambda u: u.is_staff,
        login_url='login'
    )(view_func)


# =========================
# Dashboard
# =========================
@login_required(login_url='login')
def dashboard(request):
    context = {
        "category_count": Category.objects.count(),
        "blogs_count": Blog.objects.count()
    }
    return render(request, 'dashboard/dashboard.html', context)


# =========================
# Category Management (Staff Only)
# =========================
@staff_required
def categories(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/categories.html', {'categories': categories})


@staff_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()

    return render(request, 'dashboard/add_category.html', {'form': form})


@staff_required
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'dashboard/edit_category.html', {
        'form': form,
        'category': category
    })


@staff_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":   # Secure Delete
        category.delete()
        return redirect('categories')

    return render(request, 'dashboard/delete_category.html', {
        'category': category
    })


# =========================
# Posts
# =========================
@login_required(login_url='login')
def posts(request):
    posts = Blog.objects.all()
    return render(request, 'dashboard/posts.html', {'posts': posts})


@login_required(login_url='login')
def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            post.slug = slugify(post.title) + '-' + str(post.id)
            post.save()

            return redirect('posts')
    else:
        form = BlogPostForm()

    return render(request, 'dashboard/add_post.html', {'form': form})


@login_required(login_url='login')
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)

    # Only Author or Staff can edit
    if request.user != post.author and not request.user.is_staff:
        return redirect('posts')

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.slug = slugify(post.title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'dashboard/edit_post.html', {
        'form': form,
        'post': post
    })


@login_required(login_url='login')
def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)

    # Only Author or Staff can delete
    if request.user != post.author and not request.user.is_staff:
        return redirect('posts')

    if request.method == "POST":   # Secure Delete
        post.delete()
        return redirect('posts')

    return render(request, 'dashboard/delete_post.html', {
        'post': post
    })


# =========================
# User Management (Staff Only)
# =========================
@staff_required
def users(request):
    users = User.objects.all()
    return render(request, 'dashboard/users.html', {'users': users})


@staff_required
def add_user(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = AddUserForm()

    return render(request, 'dashboard/add_user.html', {'form': form})


@staff_required
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = EditUserForm(instance=user)

    return render(request, 'dashboard/edit_user.html', {'form': form})


@staff_required
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == "POST":   # Secure Delete
        user.delete()
        return redirect('users')

    return render(request, 'dashboard/delete_user.html', {
        'user': user
    })