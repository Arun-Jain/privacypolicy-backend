from rest_framework import serializers
from .models import (
						Privacy
						)

class PrivacySerializer(serializers.ModelSerializer):
	class Meta:
		model = Privacy
		fields = ('id', 'default', 'analytics', 'third_party', 'ads', 'children_pp',)
