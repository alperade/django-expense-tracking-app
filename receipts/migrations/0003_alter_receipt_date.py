# Generated by Django 4.1.1 on 2022-09-08 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("receipts", "0002_rename_receipts_receipt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipt",
            name="date",
            field=models.DateTimeField(),
        ),
    ]
