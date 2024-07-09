# Generated by Django 5.0.1 on 2024-02-20 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('summary', models.CharField(max_length=400, verbose_name='Short Summary')),
                ('runtime', models.IntegerField(verbose_name='RUntime')),
                ('director', models.CharField(max_length=100, verbose_name='Director')),
                ('Cast', models.CharField(max_length=200, verbose_name='Cast')),
                ('poster', models.ImageField(upload_to='')),
            ],
        ),
    ]