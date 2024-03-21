from rest_framework import serializers
from .models import GLBFile

class GLBFileSerializer(serializers.ModelSerializer):
	class Meta:
		model = GLBFile
		fields = ('file',)