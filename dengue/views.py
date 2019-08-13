from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import HttpResponse, Http404, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import *
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.template import loader
import datetime
from datetime import date
from datetime import timedelta
from django import template
from dengue.models import *
from dengue.forms import *
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db import connection
from django.db.models import F
from django.db import transaction
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


	# adminpanel(CRUD)
def viewslogin(request):
	args={'log': 'active', 'hello':'e'}
	return render(request,"accounts/login.html", args)
def viewslogout(request):
	return render(request,"accounts/logout.html")


@login_required(login_url="/accounts/login/")
def activitylog(request):
	logs = LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:20]
	args = {'logs': logs, 'setlog':'active', 'set':'active'}
	return render(request, 'setting/activitylog.html', args)



@login_required(login_url="/accounts/login/")
def register(request):
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return  HttpResponse("Done...")
		else:  # form is not valid
			return HttpResponse("Form is not valid")
	else:
		form = UserCreationForm()

		args = {'form': form,'reg':'active', 'set':'active'}
		return render(request, 'accounts/reg_form.html', args)
def profile(request):
	args={'user':request.user,'setpro':'active', 'set':'active'}
	return render(request, 'accounts/profile.html', args)

#Home
def viewshome(request):
	context={
		'h':'active',
		'hh':'active'
	}
	return render(request,"viewsforall/index.html", context)