# Generated by Django 4.1.7 on 2023-02-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_blog_slug_alter_blog_ishome"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
