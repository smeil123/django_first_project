from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# Create your views here.

def post_list(request):
	# post는 쿼리셋의 이름 
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	#posts = 'test massage'
	return render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})