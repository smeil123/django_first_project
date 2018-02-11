from django.db import models
from django.utils import timezone

# 모델(객체)를 정의하는 코드
# class 는 객체 정의 키워드, Post는 모델의 이름 
# models는 Post가 장고모델임을 의미
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)	# 글자수가 제한된 텍스트를 정의할 때 사용
	text = models.TextField()	# 글자수에 제한이 없는 긴 텍스트 
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True,null=True)

	# def 는 메서드, publish는 메서드 이름 
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	# __str__를 호출하면 Post모델의 제목텍스트를 return 
	def __str__(self):
		return self.title

# Create your models here.
