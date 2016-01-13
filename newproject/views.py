from django.http import Http404 , HttpResponse
from django.template.loader import get_template
from django.template import Template , Context
from django.shortcuts import render
from blog.models import Admin 
from blog.models import Data
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    return render(request, 'file.html')

def reachhome(request):
 	return render(request,'newfile.html')

def check1(request):
	uname = request.GET.get('username')
	passwd = request.GET.get('password')
	user = authenticate(username=uname, password=passwd)
	print user
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
	post = get_object_or_404(Data, slug=slug)
	return render(request, 'post.html', {'posts':post})

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


