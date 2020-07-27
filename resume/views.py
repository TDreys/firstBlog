from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *

# Create your views here.

def view_resume(request):
	try:
		details = Details.objects.all()[0]
	except:
		details = Details()
		details.name = ''
		details.email = ''
		details.phoneNumber = ''
	finally:
		experiences = Experience.objects.all()
		educations = Education.objects.all()
		skills = Skill.objects.all()
		return render(request,'resume.html',{'details': details,
											'experiences':experiences,
											'educations':educations,
											'skills':skills,})

def edit_details(request):
	if request.method == 'POST':
		detailsFromForm = request.POST
		details = Details()
		details.name = detailsFromForm.get('name','')
		details.phoneNumber = detailsFromForm.get('phoneNumber','')
		details.email = detailsFromForm.get('email','')
		details.save()
		return redirect('view_resume')

	else:
		return render(request,'edit_details.html')

def add_experience(request):
	if request.method == 'POST':
		experienceFromForm = request.POST
		experience = Experience()
		experience.jobTitle = experienceFromForm.get('jobTitle','')
		experience.companyName = experienceFromForm.get('companyName','')
		experience.startDate = experienceFromForm.get('startDate','')
		experience.endDate = experienceFromForm.get('endDate','')
		experience.jobDescription = experienceFromForm.get('jobDescription','')
		experience.responsibilities = experienceFromForm.get('responsibilities','')
		experience.save()
		return redirect('view_resume')
	else:
		return render(request,'add_experience.html')

def add_education(request):
	if request.method == 'POST':
		educationFromForm = request.POST
		education = Education()
		education.schoolName = educationFromForm.get('schoolName','')
		education.startDate = educationFromForm.get('startDate','')
		education.endDate = educationFromForm.get('endDate','')
		education.subjects = educationFromForm.get('subjects','')
		education.save()
		return redirect('view_resume')
	else:
		return render(request,'add_education.html')

def add_skill(request):
	if request.method == 'POST':
		skillFromForm = request.POST
		skill = Skill()
		skill.skill = skillFromForm.get('skill','')

		skill.save()
		return redirect('view_resume')
	else:
		return render(request,'add_skill.html')


def remove_education(request,pk):
    toRemove = Education.objects.get(pk=pk)
    toRemove.delete()
    return redirect('view_resume')

def remove_experience(request,pk):
    toRemove = Experience.objects.get(pk=pk)
    toRemove.delete()
    return redirect('view_resume')

def remove_skill(request,pk):
    toRemove = Skill.objects.get(pk=pk)
    toRemove.delete()
    return redirect('view_resume')
