# Generated by Django 2.1.12 on 2020-01-08 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0040_merge_20200102_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='media',
        ),
    ]