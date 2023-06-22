# Generated by Django 4.1.7 on 2023-06-22 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("miniapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BillingDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("pin_code", models.CharField(max_length=10)),
                ("phone_number", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
