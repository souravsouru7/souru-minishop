# Generated by Django 4.2.1 on 2023-06-07 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0003_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="items",
        ),
    ]
