from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Blog(models.Model):
	title=models.CharField(max_length=100)
	content=RichTextUploadingField ()
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	image=models.ImageField(default='default.jpg',upload_to='profile_pics')
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('blog-detail',kwargs={'pk':self.pk})
	def yearpublished(self):
		return self.date_posted.strftime('%Y')
	def monthpublished(self):
		return self.date_posted.strftime('%m')
	def daypublished(self):
		return self.date_posted.strftime('%d')


class Notice(models.Model):
	title=models.CharField(max_length=100)
	content=RichTextUploadingField ()
	date_posted=models.DateTimeField(default=timezone.now)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('blog-detail',kwargs={'pk':self.pk})


