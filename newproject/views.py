from django.http import Http404 , HttpResponse
from django.template.loader import get_template
from django.template import Template , Context
from django.shortcuts import render
from blog.models import Admin 
from blog.models import Data
from blog.models import likes
from blog.models import comment
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
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



def check1(request):
	uname = request.GET.get('username')
	passwd = request.GET.get('password')
	if (uname and passwd) or (uname==None and passwd == None):
		user = authenticate(username=uname, password=passwd)
		login(request , user)
		data = Data.objects.all()
		if uname == None and passwd == None:
			return render(request,'newfile.html',{ 'data':data , 'x':"Logout" })
		if user:
			return render(request,'newfile.html',{ 'data':data ,'x':"Logout" })
		else:
			response="Incorrect Credentials"
		return HttpResponse(response)
	else:
		response = "enter details"
		return HttpResponse(response)



def log(request):
	if request.user.is_authenticated():
		logout(request)
		data = Data.objects.all()
		return render(request,'newfile.html',{'data':data , 'x':"Login"})
	else:
		return render(request,'file.html')


def register(request):
	return render(request,'register.html')
	
def post(request, slug):
	global post_title
	post = get_object_or_404(Data, slug=slug)
	post_title = post
	if request.user.is_authenticated():
		l = likes.objects.filter(post = post, user = request.user)
		c = comment.objects.filter(post = post)
		
		if not l:
			return render(request,'post.html',{'posts':post , 'x':"Like" , 'usr':request.user , 'y':"Logout" , 'comment':c })
		else :
			return render(request,'post.html',{'posts':post , 'x':"Unlike" , 'usr':request.user , 'y':"Logout" , 'comment':c})
		return render(request, 'post.html', {'posts':post , 'x':"Like" , 'usr':request.user , 'y':"Logout", 'comment':c })
	else:
		return render(request,'post.html',{'posts':post , 'x':"Like" , 'usr':request.user , 'y':"Login" })

def contact(request):
	if request.user.is_authenticated():
		return render(request,'contact.html',{'x':"Logout"})
	else:
		return render(request,'contact.html',{'x':"Login" })

def create(request):
	usr=request.GET.get('username')
	pswd=request.GET.get('password')
	email=request.GET.get('email')
	if usr and pswd and email:
		user = User.objects.create_user(usr,email,pswd)
		user.save()
		data = Data.objects.all()
		return render(request,'newfile.html',{ 'data':data,})
	else:
		response="enter all details"

	return HttpResponse(response)

def articles(request):
	data=Data.objects.all()
	if request.user.is_authenticated():
		return render(request,'articles.html',{ 'data':data , 'x':"Logout"})
	else : 
		return render(request,'articles.html',{'data':data , 'x':"Login" })

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
		data = Data.objects.filter(title__icontains = query)
		if request.user.is_authenticated():
			return render(request,'list.html',{'data':data , 'x':"Logout" })
		else:
			return render(request,'list.html',{'data':data , 'x':"Login" })
	else :
		response = "Enter your query"

	return HttpResponse(response)

def change1(request):
	return render(request,'change.html')

def reach(request):
	return render(request,'list.html')


def goback(request):
	if request.user.is_authenticated():
		data = Data.objects.all()
		return render(request,'newfile.html',{'data':data , 'x':"Logout" })
	else:
		data = Data.objects.all()
		return render(request,'newfile.html',{'data':data , 'x':"Login" })


def go(request):
	if request.user.is_authenticated():
		data = Data.objects.all()
		return render(request,'newfile.html',{'data':data , 'x':"Logout"})
	else:
		data = Data.objects.all()
		return render(request,'newfile.html',{'data':data , 'x':"Login"})

def like(request):
	if request.method == 'POST':
		print request.user
		print request.user.is_authenticated()
		if request.user.is_authenticated():
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
			ctx = {'likes_count':post_title.number_likes , 'x':cx}
			return HttpResponse(json.dumps(ctx), content_type='application/json')
		else :
			return render(request,'file.html')

def ret(request):
	return render(request,'file.html')

def commenting(request):
	if request.method == 'POST':
		comm = request.POST.get("comment")
		cmnt = comment.objects.filter(post = post_title)
		#import pdb; pdb.set_trace()
		if not comm == "":
			obj = comment(user = request.user, post = post_title, text = comm)
			obj.save()
			post_title.number_comments += 1
			post_title.save()
		ctx = {'num_comm':post_title.number_comments , 'usr':unicode(request.user), 'tex':unicode(comm) ,  'date':obj.date_created.strftime('%b %d, %Y ')}
		return HttpResponse(json.dumps(ctx), content_type='application/json')



