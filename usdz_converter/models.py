from django.db import models

class GLBFile(models.Model):
	file = models.FileField(upload_to='glb_files/')
	