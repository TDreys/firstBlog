from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from home.views import home_page

class homePageTest(TestCase):

	def test_root_resolves_to_home_page(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')	
		self.assertTemplateUsed(response, 'home.html')

