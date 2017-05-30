from django.shortcuts import render
from django.utils import timezone
from .models import Post 



def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

	"""
	posts1 = Post.objects.all().order_by('-published_date')
	context = {
		'posts':posts,
		'posts1':posts1,
	}
	return render(request, 'blog/post_list.html', context)
	"""
	return render(request, 'blog/post_list.html', {'posts':posts})