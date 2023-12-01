from django.db import models


class DownloadURL(models.Model):
    file_name = models.CharField(max_length=100, unique=True)
    created_by = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    url = models.URLField()
    downloaded = models.BooleanField(default=False)
    file_type = models.CharField(max_length=64)
    text_file_name = models.CharField(max_length=100, unique=True)
    text_file_path = models.CharField(max_length=100)
    loaded_to_db = models.BooleanField(default=False)

    def __str__(self):
        return self.file_name
