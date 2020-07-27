from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.

def home_page(request):
	return render(request,'home.html')
	

