from django.shortcuts import render, HttpResponse,redirect,get_object_or_404,reverse
from .models import Article, Comment

# Create your views here.

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})


def index(request):

    context ={
        "numbers":[1,2,3,4,5,6]

    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")