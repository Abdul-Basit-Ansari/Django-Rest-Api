from django.db import models

# Create your models here.

class Students(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=40)
	age = models.IntegerField()
	marks = models.IntegerField()

	class Meta:
		"""Meta definition for MODELNAME."""

		verbose_name = 'Students'
		verbose_name_plural = 'Students'

	def __str__(self):
		return str(self.id) + " " +  self.name



