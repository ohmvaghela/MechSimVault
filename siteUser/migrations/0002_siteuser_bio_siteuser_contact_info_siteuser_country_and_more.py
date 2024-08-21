# Generated by Django 5.1 on 2024-08-21 10:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='bio',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='bio'),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='contact_info',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='contact info'),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='country',
            field=models.CharField(blank=True, default='INDIA', max_length=250, verbose_name='country'),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='full_name',
            field=models.CharField(default='Default name', max_length=50, verbose_name='full name'),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='institution',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='institution'),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='role',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='role'),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='signup_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='user creation date'),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='skills',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='skills'),
        ),
    ]