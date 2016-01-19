from django.http import Http404 , HttpResponse
from django.template.loader import get_template
from django.template import Template , Context
from django.shortcuts import render
from blog.models import Admin 
from blog.models import Data
from blog.models import likes
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.views import password_reset
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
try:
    from django.utils import simplejson as json
except ImportError:
    import json

from django.views.decorators.http import require_POST

post_title= []

def home(request):
    return render(request, 'file.html')

def reachhome(request):
 	return render(request,'newfile.html')

def check1(request):
	uname = request.GET.get('username')
	passwd = request.GET.get('password')
	user = authenticate(username=uname, password=passwd)
	login(request , user)
	data = Data.objects.all()
	if uname == None and passwd == None:
		return render(request,'newfile.html',{ 'data':data })
	if user:
		return render(request,'newfile.html',{ 'data':data })
	else:
		response="Incorrect Credentials"
	return HttpResponse(response)

def register(request):
	return render(request,'register.html')
	
def post(request, slug):
	global post_title
	post = get_object_or_404(Data, slug=slug)
	post_title = post
	l = likes.objects.filter(post = post, user = request.user)
	if not l:
		return render(request,'post.html',{'posts':post , 'x':"Like"})
	else :
		return render(request,'post.html',{'posts':post , 'x':"Unlike"})
	return render(request, 'post.html', {'posts':post , 'x':"Like"})

def contact(request):
	return render(request,'contact.html')

def create(request):
	usr=request.GET.get('username')
	pswd=request.GET.get('password')
	email=request.GET.get('email')
	if usr and pswd and email:
		user = User.objects.create_user(usr,email,pswd)
		user.save()
		data = Data.objects.all()
		return render(request,'newfile.html',{ 'data':data})
	else:
		response="enter all details"

	return HttpResponse(response)

def articles(request):
	data=Data.objects.all()
	return render(request,'articles.html',{ 'data':data })

def change(request):
	user = request.GET.get('username')
	newp = request.GET.get('newpasswd')
	if user and newp:
		u = User.objects.get(username=user)
		u.set_password(newp)
		u.save()
		data=Data.objects.all()
		return render(request,'newfile.html',{ 'data':data })
	else:
		response="Enter details"
	return HttpResponse(response)

def search(request):
	query = request.GET.get('q')
	if query:
		flag = 1
		data = Data.objects.filter(title__icontains = query)
		return render(request,'list.html',{'data':data})
	else :
		response = "Enter your query"

	return HttpResponse(response)

def change1(request):
	return render(request,'change.html')

def reach(request):
	return render(request,'list.html')

def logout(request):
	logout(request)

def goback(request):
	data = Data.objects.all()
	return render(request,'newfile.html',{ 'data':data })

def forgot(request):
	return render(request,'passwordreset.html')

# def like_post(request):
# 	l = likes.objects.filter(user = request.user , post = post_title)
# 	if not l:
# 		post_title.number_likes += 1
# 		like = likes.objects.create(user=request.user , post = post_title)
# 		post_title.save()
# 	else:
# 		post_title.number_likes -= 1
# 		like = likes.objectls.filter(user=request.user , post = post_title)
# 		like.delete()
# 		post_title.save()
# 	return post(request, post_title.slug)

def like(request):
	if request.method == 'POST':
		l = likes.objects.filter(user= request.user, post = post_title)
		if not l:
			post_title.number_likes += 1
			like = likes.objects.create(user=request.user, post = post_title)
			post_title.save()
			cx = "Unlike"
		else:
			post_title.number_likes -= 1
			like = likes.objects.filter(user=request.user , post= post_title)
			like.delete()
			post_title.save()
			cx = "Like"
	print "blah blha"
	ctx = {'likes_count':post_title.number_likes , 'x':cx}
	return HttpResponse(json.dumps(ctx), content_type='application/json')
