# Generated by Django 4.2.7 on 2023-12-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_v1", "0004_downloadurl_file_type_downloadurl_loaded_to_db_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="downloadurl",
            name="file_type",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]