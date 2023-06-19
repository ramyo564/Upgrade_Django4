# Generated by Django 4.2.1 on 2023-05-31 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_alter_account_phone_number"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("address_line_1", models.CharField(blank=True, max_length=100)),
                ("address_line_2", models.CharField(blank=True, max_length=100)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, upload_to="userprofile"),
                ),
                ("city", models.CharField(blank=True, max_length=20)),
                ("state", models.CharField(blank=True, max_length=20)),
                ("country", models.CharField(blank=True, max_length=20)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
