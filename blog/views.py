from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from django.core import serializers
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('complete/')
    else:
        form = UserCreationForm()

    token = {}
    token.update(csrf(request))
    token['form'] = form
    return render_to_response('blog/registration_form.html',token)


def registration_complete(request):
    return render_to_response('blog/registration_complete.html')

# Lists all the blog
def post_list(request):
    posts = Post.objects.all()
    data = serializers.serialize("json", posts)
    return HttpResponse(data, content_type="application/json")


# Blog detail
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = serializers.serialize('json', [post, ])
    return HttpResponse(data, content_type="application/json")


# Saves the edit blog in the database
def save_edit_blog(request):
    blog_id = request.POST['blog-id']
    blog_text = request.POST['blog-text']
    try:
        Post.objects.filter(pk=blog_id).update(text=blog_text)
        return render(request, 'blog/post_list.html')
    except Post.DoesNotExist:
        print("Error")
        return render(request, 'An error occurred')


# Delete blog from the database
def delete_blog(request, pk):
    try:
        Post.objects.filter(pk=pk).delete()
        return render(request, 'blog/post_list.html')
    except Post.DoesNotExist:
        print("Error")
        return render(request, 'An error occurred')


# Create blog in the database
def create_blog(request):
    if request.method == "POST":
        me = User.objects.get(username='admin')
        title = request.POST['title']
        blog_text = request.POST['blog-text']
        Post.objects.create(author=me, title=title, text=blog_text)
        return HttpResponseRedirect(reverse('post_list_page'))


# Renders the blog listing page
def post_list_page(request):
    return render(request, 'blog/post_list.html')


# Renders the blog details page
def post_detail_page(request):
    return render(request, 'blog/post_detail.html')


# Renders the create blog page
def create_blog_page(request):
    return render(request, 'blog/create_blog.html')

