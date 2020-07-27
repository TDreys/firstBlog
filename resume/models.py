from django.db import models

# Create your models here.

class Details(models.Model):
	name = models.CharField(max_length=200)
	phoneNumber = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)

	def save(self, *args, **kwargs):
		try:
			toOverwrite = Details.objects.all()
			toOverwrite.delete()

		finally:
			return super().save(*args, **kwargs)

class Experience(models.Model):
	jobTitle = models.CharField(max_length=200)
	companyName = models.CharField(max_length=200)
	startDate = models.CharField(max_length=200)
	endDate = models.CharField(max_length=200)
	jobDescription = models.TextField()
	responsibilities =  models.TextField()

class Education(models.Model):
	schoolName = models.CharField(max_length=200)
	startDate = models.CharField(max_length=200)
	endDate = models.CharField(max_length=200)
	subjects = models.TextField()

class Skill(models.Model):
	skill = models.CharField(max_length=200)
