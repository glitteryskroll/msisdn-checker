# Generated by Django 4.2.4 on 2024-05-19 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("def_number", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phoneprovider",
            name="snA",
            field=models.DecimalField(decimal_places=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name="phoneprovider",
            name="snB",
            field=models.DecimalField(decimal_places=0, max_digits=20),
        ),
    ]