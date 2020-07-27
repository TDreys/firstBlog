from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from resume.views import *
from resume.models import *

class resumePageTest(TestCase):

	def test_resume_url_resolves_to_resume_page(self):
		found = resolve('/resume/')
		self.assertEqual(found.func, view_resume)

	def test_home_page_returns_correct_html(self):
		response = self.client.get('/resume/')
		self.assertTemplateUsed(response, 'resume.html')

	def test_edit_details_url_resolves_to_edit_details_page(self):
		found = resolve('/resume/editDetails')
		self.assertEqual(found.func, edit_details)

	def test_edit_details_page_returns_correct_html(self):
		response = self.client.get('/resume/editDetails')
		self.assertTemplateUsed(response,'edit_details.html')

	def test_edit_details_redirects_on_submit(self):
		details = {'name':'test','phoneNumber':'11111','email':'test@test.com'}
		response = self.client.post('/resume/editDetails',data = details)
		self.assertEqual(response.url,'/resume/')

	def test_saving_and_retrieving_details(self):
		details = Details()
		details.name = 'testName'
		details.phoneNumber = '11111'
		details.email = 'test@test.com'
		details.save()

		saved_details = Details.objects.all()

		self.assertEqual(saved_details.count(),1)
		self.assertEqual(saved_details[0],details)

	def test_only_single_details_model_can_exist(self):
		details = Details()
		details.name = 'existing'
		details.phoneNumber = '11111'
		details.email = 'existing@test.com'
		details.save()

		details2 = Details()
		details2.name = 'overwrite'
		details2.phoneNumber = '111112'
		details2.email = 'overwrite@test.com'
		details2.save()

		saved_details = Details.objects.all()

		self.assertEqual(saved_details.count(),1)
		self.assertEqual(saved_details[0],details2)

	def test_details_save_when_submitted(self):
		details = {'name':'test','phoneNumber':'11111','email':'test@test.com'}
		response = self.client.post('/resume/editDetails',data = details)

		saved_details = Details.objects.all()

		self.assertEqual(saved_details.count(),1)
		self.assertEqual(saved_details[0].name,'test')
		self.assertEqual(saved_details[0].phoneNumber,'11111')
		self.assertEqual(saved_details[0].email,'test@test.com')

	def test_add_experience_url_resolves_to_edit_details_page(self):
		found = resolve('/resume/addExperience')
		self.assertEqual(found.func, add_experience)

	def test_add_experience_page_returns_correct_html(self):
		response = self.client.get('/resume/addExperience')
		self.assertTemplateUsed(response,'add_experience.html')

	def test_edit_details_redirects_on_submit(self):
		response = self.client.post('/resume/addExperience')
		self.assertEqual(response.url,'/resume/')

	def test_saving_and_retrieving_experience(self):
		experience = Experience()
		experience.jobTitle = 'test title'
		experience.companyName = 'test company'
		experience.startDate = '01-01-2018'
		experience.endDate = '01-02-2018'
		experience.jobDescription = 'test description'
		experience.responsibilities = 'test responsibilities'
		experience.save()

		saved_experience = Experience.objects.all()

		self.assertEqual(saved_experience.count(),1)
		self.assertEqual(saved_experience[0],experience)

	def test_experience_saves_when_submitted(self):
		experience = {'jobTitle':'test title',
					'companyName':'test company',
					'startDate':'01-01-2018',
					'endDate':'01-02-2018',
					'jobDescription':'test description',
					'responsibilities':'test responsibilities'}

		response = self.client.post('/resume/addExperience',data = experience)

		saved_experience = Experience.objects.all()

		self.assertEqual(saved_experience[0].jobTitle,'test title')
		self.assertEqual(saved_experience[0].companyName,'test company')
		self.assertEqual(saved_experience[0].startDate,'01-01-2018')
		self.assertEqual(saved_experience[0].endDate,'01-02-2018')
		self.assertEqual(saved_experience[0].jobDescription,'test description')
		self.assertEqual(saved_experience[0].responsibilities,'test responsibilities')

	def test_can_delete_experience(self):
		experience = Experience()
		experience.jobTitle = 'test title'
		experience.companyName = 'test company'
		experience.startDate = '01-01-2018'
		experience.endDate = '01-02-2018'
		experience.jobDescription = 'test description'
		experience.responsibilities = 'test responsibilities'
		experience.save()

		self.assertEqual(Experience.objects.all().count(),1)
		self.client.get('/resume/removeExperience/1')
		self.assertEqual(Experience.objects.all().count(),0)

	def test_add_education_url_resolves_to_edit_details_page(self):
		found = resolve('/resume/addEducation')
		self.assertEqual(found.func, add_education)

	def test_add_education_page_returns_correct_html(self):
		response = self.client.get('/resume/addEducation')
		self.assertTemplateUsed(response,'add_education.html')

	def test_add_education_redirects_on_submit(self):
		response = self.client.post('/resume/addEducation')
		self.assertEqual(response.url,'/resume/')

	def test_saving_and_retrieving_education(self):
		education = Education()
		education.schoolName = 'Univeristy of Birmingham'
		education.startDate = '01-01-2018'
		education.endDate = 'present'
		education.subjects = 'Bsc Computer Science'
		education.save()

		saved_education = Education.objects.all()

		self.assertEqual(saved_education.count(),1)
		self.assertEqual(saved_education[0],education)

	def test_education_saves_when_submitted(self):
		education = {'schoolName':'university of birmingham',
					'startDate':'01-01-2018',
					'endDate':'present',
					'subjects':'bsc computer science'}

		response = self.client.post('/resume/addEducation',data = education)

		saved_education = Education.objects.all()

		self.assertEqual(saved_education[0].schoolName,'university of birmingham')
		self.assertEqual(saved_education[0].startDate,'01-01-2018')
		self.assertEqual(saved_education[0].endDate,'present')
		self.assertEqual(saved_education[0].subjects,'bsc computer science')

	def test_can_delete_education(self):
		education = Education()
		education.schoolName = 'Univeristy of Birmingham'
		education.startDate = '01-01-2018'
		education.endDate = 'present'
		education.subjects = 'Bsc Computer Science'
		education.save()

		self.assertEqual(Education.objects.all().count(),1)
		self.client.get('/resume/removeEducation/1')
		self.assertEqual(Education.objects.all().count(),0)

	def test_add_skill_url_resolves_to_edit_details_page(self):
		found = resolve('/resume/addSkill')
		self.assertEqual(found.func, add_skill)

	def test_add_skill_page_returns_correct_html(self):
		response = self.client.get('/resume/addSkill')
		self.assertTemplateUsed(response,'add_skill.html')

	def test_add_skill_redirects_on_submit(self):
		response = self.client.post('/resume/addSkill')
		self.assertEqual(response.url,'/resume/')

	def test_saving_and_retrieving_skill(self):
		skill = Skill()
		skill.skill = 'Django'
		skill.save()

		saved_skill = Skill.objects.all()

		self.assertEqual(saved_skill.count(),1)
		self.assertEqual(saved_skill[0],skill)

	def test_skill_saves_when_submitted(self):
		skill = {'skill':'Django'}

		response = self.client.post('/resume/addSkill',data = skill)

		saved_skill = Skill.objects.all()

		self.assertEqual(saved_skill[0].skill,'Django')

	def can_delete_skill(self):
		skill = Skill()
		skill.skill = 'Django'
		skill.save()

		self.assertEqual(Skill.objects.all().count(),1)
		self.client.get('/resume/removeSkill/1')
		self.assertEqual(Skill.objects.all().count(),0)
