# Generated by Django 4.2.1 on 2023-06-02 17:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receipts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipt",
            name="date",
            field=models.DateTimeField(),
        ),
    ]
