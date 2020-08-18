from django import template

register = template.Library() 
from blog.models import Blog
@register.inclusion_tag('users/blog_title.html')
def title(user,context=True):
	blog=Blog.objects.filter(author=user)
	return{'blog':blog}

#@register.simple_tag
#def trys(user,context=True):
	#blog=Blog.objects.filter(author=user)
	#return{'blog':blog}

@register.simple_tag
def urls(user):
	if user.first_name=='teacher':
		url= 'profile/'
		return url

	else:
		exists=hasattr(user, 'studentinfo')
		if exists:
			return f"student/profile/{user.studentinfo.id}"

		else:
			return "student/profile/"