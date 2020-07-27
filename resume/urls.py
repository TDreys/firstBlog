from django.urls import path
from . import views

urlpatterns = [
	path('', views.view_resume, name='view_resume'),
	path('editDetails', views.edit_details, name='edit_details'),
	path('addExperience', views.add_experience, name='add_experience'),
	path('addEducation',views.add_education, name = 'add_education'),
	path('addSkill',views.add_skill, name = 'add_skill'),
    path('removeEducation/<int:pk>',views.remove_education, name = 'remove_education'),
    path('removeExperience/<int:pk>',views.remove_experience, name = 'remove_experience'),
    path('removeSkill/<int:pk>',views.remove_skill, name = 'remove_skill'),
]
