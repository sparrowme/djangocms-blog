# Generated by Django 1.11.24 on 2019-09-14 10:45

import django.db.models.deletion
from django.db import migrations, models

import djangocms_blog.media.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cms", "0020_old_tree_cleanup"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vimeo",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="media_app_vimeo",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                ("url", models.URLField(verbose_name="Video URL")),
            ],
            options={
                "abstract": False,
            },
            bases=(djangocms_blog.media.base.MediaAttachmentPluginMixin, "cms.cmsplugin"),
        ),
        migrations.CreateModel(
            name="YoutTubeVideo",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="media_app_youttubevideo",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                ("url", models.URLField(verbose_name="video URL")),
            ],
            options={
                "abstract": False,
            },
            bases=(djangocms_blog.media.base.MediaAttachmentPluginMixin, "cms.cmsplugin"),
        ),
    ]
