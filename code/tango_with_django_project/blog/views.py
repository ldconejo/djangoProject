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

# View to add new blog entries
def add_entry(request, category_name_url):
    # Get the context from the request
    context = RequestContext(request)

    # Check if the request is HTTP POST
    if request.method == 'POST':
        form = BlogForm(request.POST)

        if form.is_valid():
            # Do not commit yet, as category needs to be populated
            entry = form.save(commit=False)

            # Retrieve the associated category and verify that it exists
            #try:
            cat = Category.objects.get(title=category_name_url)
            entry.category = cat
            #except:
                # Category doesn't exist and the user will be asked to create it
            #    return render_to_response('blog/add_category.html', {}, context)

            # Now that we know the category exists, we can save the entry
            entry.save()

            # Now that the page is saved, display the category instead
            return view_category(request, category_name_url)
        else:
            print form.errors
    else:
        form = BlogForm()

    return render_to_response('blog/add_entry.html',
                              { 'category_name_url': category_name_url,
                                'form': form},
                              context)

# Delete an existing blog entry
def delete_entry(request, category_name_url, slug):
    return render_to_response('blog/view_post.html', {
        'category': category_name_url,
        # Gets the object that will be destroyed
        'post': get_object_or_404(Blog, slug=slug),
    })

    # Check if the request is HTTP POST

# This one converts the URL category name to a simple category name
# Note that in its simplest implementation, this simply removes the underscores (_)
# from the category name
def decode_url(category_name_url):
    result = category_name_url.replace("_", " ")
    return result

def index(request):
    return render_to_response('blog/index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, category_name_url, slug):
    return render_to_response('blog/view_post.html',{
        'post': get_object_or_404(Blog, slug=slug),
        'category': category_name_url
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })