# Generated by Django 4.1.7 on 2023-02-23 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_alter_blog_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.category",
            ),
        ),
    ]