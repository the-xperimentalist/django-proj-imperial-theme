from django.db import models

class Service(models.Model):
	service_title = models.CharField(max_length=200)
	service_logo = models.CharField(max_length=50)
	service_descripion = models.CharField(max_length=600)

	def __str__(self):
		return self.service_title

class Portfolio(models.Model):
	portfolio_title = models.CharField(max_length=200)
	portfolio_description = models.CharField(max_length=200)
	portfolio_img_src = models.CharField(max_length=400)

	def __str__(self):
		return self.portfolio_title
