from rest_framework import viewsets
from rest_framework.response import Response
from subprocess import Popen, PIPE
from django.http import HttpResponse
from .models import GLBFile
from .serializers import GLBFileSerializer

class GLBFileViewSet(viewsets.ViewSet):
	def create(self, request):
		serializer = GLBFileSerializer(data=request.data)
		if serializer.is_valid():
			glb_file = serializer.save()
			usdz_filename = f'{glb_file.file.name.split(".")[0]}.usdz'
			process = Popen(['usdzconvert', glb_file.file.path, usdz_filename], stdout=PIPE, stderr=PIPE)
			stdout, stderr = process.communicate()
			if stderr:
				return Response({'error': stderr.decode('utf-8')}, status=400)
			with open(usdz_filename, 'rb') as usdz_file:
				response = HttpResponse(usdz_file.read(), content_type='application/octet-stream')
				response['Content-Disposition'] = f'attachment; filename="{usdz_filename}"'
				return response
		else:
			return Response(serializer.errors, status=400)
