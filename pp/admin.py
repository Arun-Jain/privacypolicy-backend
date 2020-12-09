from django.contrib import admin
from .models import Privacy

@admin.register(Privacy)
class NewsTypesAdmin(admin.ModelAdmin):
	list_display = ("id", "default", "analytics", "third_party", "ads", "children_pp",)
	# list_filter = ("news_type",)
	search_fields = ("id",)
