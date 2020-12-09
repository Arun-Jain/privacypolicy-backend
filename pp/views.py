from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
# from django.core.mail import send_mail
from .models import Privacy

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from .serializers import PrivacySerializer
import json

from .utils import render_to_pdf
from django.template.loader import get_template
import base64
from io import BytesIO

# from weasyprint import HTML



@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def privacyPolicy(request):
	
	if request.method == "POST":

		email = request.POST.get('email')
		if not email:
			return Response({'response': 'Please provide email_id'}, status=status.HTTP_400_BAD_REQUEST)

		contact = request.POST.get('contact')
		if not contact:
			return Response({'response': 'Please provide contact number'}, status=status.HTTP_400_BAD_REQUEST)

		site_url = request.POST.get('url')
		# if not site_url:
		# 	return Response({'response': 'Please provide site url'}, status=status.HTTP_400_BAD_REQUEST)

		site_name = request.POST.get('name')
		app_name = request.POST.get('app')
		# if not site_name:
		# 	return Response({'response': 'Please provide site name'}, status=status.HTTP_400_BAD_REQUEST)

		ads = request.POST.get('ads')
		analytics = request.POST.get('analytics')
		marketing = request.POST.get('marketing')

		print(request.data)

		template = get_template('privacy-policy.html')
		data = {
			'site_name': site_name,
			'site_url': site_url,
			'app_name': app_name,
			'email': email,
			'ads': ads,
			'analytics': analytics,
			'marketing': marketing,
			}
		html = template.render(data)
		html = html.replace('\n', '')
		html = html.replace('\t', '')
		# pdf = render_to_pdf('privacy-policy.html', data)

		# with open(pdf, "rb") as pdf_file:
		# 	encoded_string = base64.b64encode(pdf_file.read())

		# print(encoded_string)


		# data = Privacy.objects.all()
		# serializer = PrivacySerializer(data, many=True)
		# response_data = serializer.data

		# res = []

		# for items in response_data[0].values():
		# 	res.append(str(items).replace("<Website URL/App Name>", site_url))

		# res = {"data": res}

		# print(response_data[0]["default"].replace("<Website Name/App Name>", site_url))
		# str(response_data).replace("<Website Name/App Name>", site_url)
		# print(response_data)

		

		# return response
		return Response({"pdf_data": html}, status=status.HTTP_200_OK)
