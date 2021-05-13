from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

posts = [
    {
        'author': 'Michal',
        'title': 'Post 1',
        'content': 'This is content of post 1.',
        'date_posted': 'August 8, 2021'
    },
{
        'author': 'Karolcia',
        'title': 'Post 2',
        'content': 'This is content of post 2.',
        'date_posted': 'August 9, 2021'
    }
]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'This website is about'})
