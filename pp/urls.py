from django.urls import path, include
from privacypolicy import urls
from . import views

urlpatterns = [
	path(r'privacy', views.privacyPolicy, name="privacy_policy"),
]
