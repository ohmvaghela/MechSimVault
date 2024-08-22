# Generated by Django 5.1 on 2024-08-21 13:32

import siteUser.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteUser', '0003_siteuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_picture/base.jpg', null=True, upload_to=siteUser.models.PathAndRename()),
        ),
    ]