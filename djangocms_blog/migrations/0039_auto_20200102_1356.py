# Generated by Django 2.1.12 on 2020-01-02 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0038_blogcategory_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='blog_categories', to='djangocms_blog.BlogCategory', verbose_name='category'),
        ),
    ]
