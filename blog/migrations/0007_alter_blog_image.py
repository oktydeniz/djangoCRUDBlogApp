# Generated by Django 4.1.7 on 2023-02-22 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_category_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(upload_to="blogs"),
        ),
    ]
