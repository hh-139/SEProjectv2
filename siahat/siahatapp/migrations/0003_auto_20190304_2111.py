# Generated by Django 2.1.7 on 2019-03-04 16:11

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('siahatapp', '0002_attractions_r_menu_restaurants_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='attractions',
            name='url_Picture',
            field=django_mysql.models.ListTextField(models.CharField(blank=True, max_length=100, null=True), default='1', size=100),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='url_Picture',
            field=django_mysql.models.ListTextField(models.CharField(blank=True, max_length=100, null=True), default='1', size=100),
        ),
    ]
