# Generated by Django 2.1.7 on 2019-03-03 14:46

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('url_Picture', django_mysql.models.ListTextField(models.CharField(max_length=100), size=100)),
                ('address', models.TextField(blank=True, null=True)),
                ('star_Rating', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Hotels',
            },
        ),
    ]
