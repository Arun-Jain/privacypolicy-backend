from django.db import models

# Create your models here.
class Privacy(models.Model):
	default = models.CharField(max_length=10000, null=False, blank=False)
	analytics = models.CharField(max_length=10000, null=False, blank=False)
	third_party = models.CharField(max_length=10000, null=False, blank=False)
	ads = models.CharField(max_length=10000, null=False, blank=False)
	children_pp = models.CharField(max_length=10000, null=False, blank=False)

	class Meta:
		db_table = 'privacy policy'
