# Generated by Django 2.2.2 on 2019-06-18 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190617_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewtext',
            name='background_img',
        ),
        migrations.RemoveField(
            model_name='viewtext',
            name='content',
        ),
        migrations.AddField(
            model_name='viewtext',
            name='template_name',
            field=models.CharField(blank=True, max_length=64, unique=True),
        ),
    ]