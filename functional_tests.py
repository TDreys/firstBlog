from selenium import webdriver
import unittest
import time

class VisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_open_page(self):
		#user goes to site and lands on homepage
		self.browser.get('http://127.0.0.1:8000')

		#user notices the title of the page is 'Home'
		self.assertIn('Home', self.browser.title)

	def test_can_goto_blog(self):
		#user goes to site and lands on homepage
		self.browser.get('http://127.0.0.1:8000')

		#user sees the link to go to blog and clicks it
		blogButton = self.browser.find_element_by_id('blogLink')
		blogButton.click()

		#user notices the url has changed
		self.assertEqual('http://127.0.0.1:8000/blog/', self.browser.current_url)

	def test_can_edit_resume_details(self):
		#user goes to site and lands on homepage
		self.browser.get('http://127.0.0.1:8000')

		#user sees the link to go to resume and clicks it
		resumeButton = self.browser.find_element_by_id('resumeLink')
		resumeButton.click()

		#user notices the title of the webpage is 'Resume'
		self.assertEqual('http://127.0.0.1:8000/resume/', self.browser.current_url)

		#user clicks the edit details link
		editDetailsLink = self.browser.find_element_by_id('editDetailsLink')
		editDetailsLink.click()

		self.assertEqual('http://127.0.0.1:8000/resume/editDetails', self.browser.current_url)

		#user enters their name into the name text box
		nameInputBox = self.browser.find_element_by_id('nameInputBox')
		nameInputBox.send_keys('Test Name')

		#user enters their phone number into the phone number text box
		phoneInputBox = self.browser.find_element_by_id('phoneInputBox')
		phoneInputBox.send_keys('11111111111')

		#user enters their email into the email text box
		emailInputBox = self.browser.find_element_by_id('emailInputBox')
		emailInputBox.send_keys('testemail@test.com')

		#user clicks enter and is sent back to the resume page
		submitButton = self.browser.find_element_by_id('submitButton')
		submitButton.submit()

		time.sleep(1)

		self.assertEqual('http://127.0.0.1:8000/resume/', self.browser.current_url)

		#the details on the resume page have been updated
		name = self.browser.find_element_by_id('nameParagraph')
		contacts = self.browser.find_elements_by_class_name('contact-details')

		self.assertEqual(name.text,'Test Name')
		self.assertEqual(contacts[0].text,'Email:\ntestemail@test.com\nPhone:\n11111111111')

	def test_can_add_experience(self):
		#user goes to resume page
		self.browser.get('http://127.0.0.1:8000/resume/')

		#the user wants to add two previous experiences
		for i in range(2):
			#user sees the add experience link and clicks it
			addExperienceLink = self.browser.find_element_by_id('addExperienceLink')
			addExperienceLink.click()
			self.assertEqual('http://127.0.0.1:8000/resume/addExperience', self.browser.current_url)

			#user enters the job title
			jobTitleField = self.browser.find_element_by_id('jobTitleField')
			jobTitleField.send_keys('test job title ' + str(i))

			#user enters the company name
			companyNameField = self.browser.find_element_by_id('companyNameField')
			companyNameField.send_keys('Test Company ' + str(i))

			#user enters the start and end dates
			startDateField = self.browser.find_element_by_id('startDateField')
			endDateField = self.browser.find_element_by_id('endDateField')

			if i == 0:
				startDateField.send_keys('01-01-2017')
				endDateField.send_keys('01-02-2018')
			else:
				startDateField.send_keys('01-03-2018')
				endDateField.send_keys('Present')

			#user enters the job description
			jobDescriptionField = self.browser.find_element_by_id('jobDescriptionField')
			jobDescriptionField.send_keys('test job description ' + str(i))

			#user enters responsibilities and achievements
			responsibilitiesField = self.browser.find_element_by_id('responsibilitiesField')
			responsibilitiesField.send_keys('test responsibility ' + str(i))

			#user submits the form and is redirected to the resume page
			submitButton = self.browser.find_element_by_id('submitButton')
			submitButton.submit()

			time.sleep(1)

		#the user sees the new experience along with any others that were already there
		jobTitles = self.browser.find_elements_by_class_name('jobTitles')
		companyNames = self.browser.find_elements_by_class_name('companyNames')
		dates = self.browser.find_elements_by_class_name('dates')
		jobDescriptions = self.browser.find_elements_by_class_name('jobDescriptions')
		responsibilities = self.browser.find_elements_by_class_name('responsibilities')

		self.assertIn('test job title 0',[x.text for x in jobTitles])
		self.assertIn('test job title 1',[x.text for x in jobTitles])
		self.assertIn('Test Company 0',[x.text for x in companyNames])
		self.assertIn('Test Company 1',[x.text for x in companyNames])
		self.assertIn('01-01-2017 - 01-02-2018',[x.text for x in dates])
		self.assertIn('01-03-2018 - Present',[x.text for x in dates])
		self.assertIn('test job description 0',[x.text for x in jobDescriptions])
		self.assertIn('test job description 1',[x.text for x in jobDescriptions])
		self.assertIn('test responsibility 0',[x.text for x in responsibilities])
		self.assertIn('test responsibility 1',[x.text for x in responsibilities])

	def test_can_add_education(self):
		#user goes to resume page
		self.browser.get('http://127.0.0.1:8000/resume/')

		#user clicks the add education link
		addEducationLink = self.browser.find_element_by_id('addEducationLink')
		addEducationLink.click()
		self.assertEqual('http://127.0.0.1:8000/resume/addEducation', self.browser.current_url)

		#user enters the schools name
		schoolNameField = self.browser.find_element_by_id('schoolNameField')
		schoolNameField.send_keys('University of Birmingham')

		#user enters the start and end dates
		startDateField = self.browser.find_element_by_id('startDateField')
		endDateField = self.browser.find_element_by_id('endDateField')
		startDateField.send_keys('01-01-2017')
		endDateField.send_keys('present')

		#user enters degree or subject names, as well as any extra information
		subjectsField = self.browser.find_element_by_id('subjectsField')
		subjectsField.send_keys('Bsc Computer Science')

		#user submits the form and is redirected to the resume page
		submitButton = self.browser.find_element_by_id('submitButton')
		submitButton.submit()

		time.sleep(1)

		#user notices that the education details have been added
		schoolNames = self.browser.find_elements_by_class_name('schoolNames')
		dates = self.browser.find_elements_by_class_name('dates')
		subjects = self.browser.find_elements_by_class_name('subjects')

		self.assertIn('University of Birmingham',[x.text for x in schoolNames])
		self.assertIn('01-01-2017 - present',[x.text for x in dates])
		self.assertIn('Bsc Computer Science',[x.text for x in subjects])

	def test_can_add_skill(self):
		#user goes to resume page
		self.browser.get('http://127.0.0.1:8000/resume/')

		#user clicks link to add skill
		addSkillLink = self.browser.find_element_by_id('addSkillLink')
		addSkillLink.click()
		self.assertEqual('http://127.0.0.1:8000/resume/addSkill', self.browser.current_url)

		#user enters a skill
		skillField = self.browser.find_element_by_id('skillField')
		skillField.send_keys('Django')

		#user submits the form and is redirected to resume page
		submitButton = self.browser.find_element_by_id('submitButton')
		submitButton.submit()

		time.sleep(1)

		#user notices the skill has been added
		skills = self.browser.find_elements_by_class_name('skills')

		self.assertIn('- Django',[x.text for x in skills])


if __name__ == '__main__':
    unittest.main(warnings='ignore')
