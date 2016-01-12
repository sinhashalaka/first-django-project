from django.http import Http404 , HttpResponse
from django.template.loader import get_template
from django.template import Template , Context
from django.shortcuts import render
import datetime
from blog.models import Admin 
from blog.models import Data
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

flag = 0

def home(request):
    return render(request, 'file.html')

def check1(request):
	uname = request.GET.get('username')
	passwd = request.GET.get('password')
	if (uname and passwd) or (uname == None and passwd == None):
		if(uname == None and passwd == None):
			data = Data.objects.all()
			return render(request,'newfile.html', { 'data':data })
		else:
			try:
				adm = Admin.objects.get(name=uname)
			except:
				adm = None
			if (adm == None):
				response = "Wrong username"

			else:
				if adm.password == passwd:
			#response="yoyo"
					data = Data.objects.all()
					return render(request,'newfile.html', { 'data':data })
				else:
					response = "Wrong Password"
		
	else:
		response = "not logged in"
		
	return HttpResponse(response)
	
def post(request, slug):
	post = get_object_or_404(Data, slug=slug)
	return render(request, 'post.html', {'posts':post})

def contact(request):
	return render(request,'contact.html')

def articles(request):
	data=Data.objects.all()
	return render(request,'articles.html',{ 'data':data })

def search(request):
	query = request.GET.get('q')
	if query:
		flag = 1
		data = Data.objects.filter(title__icontains = query)
		return render(request,'list.html',{'data':data})
	else :
		response = "Enter your query"

	return HttpResponse(response)

def reach(request):
	return render(request,'list.html')


