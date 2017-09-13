from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article

def home(request):
	return HttpResponse('Hello World')


def detail(request, bid):
	blog = Article.objects.all()[int(bid)]
	str = "title = %s, category = %s, datetime = %s, content = %s" % (
		blog.title, blog.category, blog.date_time, blog.content)
	return HttpResponse(str)
