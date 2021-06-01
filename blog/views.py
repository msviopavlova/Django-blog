from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'ViolettaP',
        'title': 'Blog Post 1',
        'content': 'My first post about Programming',
        'date_posted': 'June 1, 2021'
     },
    {
        'author': 'ViolettaP',
        'title': 'Second dummy post',
        'content': 'Very interesting information',
        'date_posted': 'May 13, 2021'
    }
]


def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})