from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_open_page(self):
		self.browser.get('http://127.0.0.1:8000')
		self.assertIn('Django', self.browser.title) 
		self.fail('finish test')

if __name__ == '__main__':  
    unittest.main(warnings='ignore')