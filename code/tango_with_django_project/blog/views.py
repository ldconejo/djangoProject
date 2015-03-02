# Create your views here.

from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.forms import BlogForm, CategoryForm

def add_category(request):
    # Get the context from the request
    context = RequestContext(request)

    # Check if the request is HTTP POST
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details
        form = CategoryForm()

    # Render the form, including any error messages
    return render_to_response('blog/add_category.html', {'form': form}, context)

def index(request):
    return render_to_response('blog/index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, slug):
    return render_to_response('blog/view_post.html',{
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })