# Generated by Django 4.1.1 on 2022-09-08 17:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("receipts", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Receipts",
            new_name="Receipt",
        ),
    ]
