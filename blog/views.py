from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import ContactForm
from django.db.models import Q


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post-detail.html', {'post': post})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect('/')

    else:
        form = ContactForm()
        # print(form)
    return render(request, 'blog/contact.html', {'form': form})


def search(request):
    search_posts = request.GET.get('q')
    if search_posts:
        posts = Post.objects.filter(Q(title__icontains=search_posts))

    return render(request, 'blog/search.html', {'posts': posts})
