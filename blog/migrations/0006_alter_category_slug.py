# Generated by Django 4.1.7 on 2023-02-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_category_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, default="", editable=False),
        ),
    ]
