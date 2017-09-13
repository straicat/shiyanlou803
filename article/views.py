from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article

def home(request):
	post_list = Article.objects.all()
	return render(request, 'home.html', {'post_list': post_list})


def detail(request, post_id):
	post = Article.objects.get(id=int(post_id))
	return render(request, 'post.html', {'post': post})
