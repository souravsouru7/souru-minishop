# Generated by Django 4.2.1 on 2023-06-02 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartitem",
            name="cart",
        ),
        migrations.RemoveField(
            model_name="cartitem",
            name="product",
        ),
        migrations.DeleteModel(
            name="Cart",
        ),
        migrations.DeleteModel(
            name="CartItem",
        ),
    ]
