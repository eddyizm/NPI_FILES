from django.contrib import admin
from api_v1.models import DownloadURL
# Register your models here.

@admin.register(DownloadURL)
class DownloadURLAdmin(admin.ModelAdmin):
    list_display = ['file_name', 'created_by', 'created_at', 'url', 'downloaded']