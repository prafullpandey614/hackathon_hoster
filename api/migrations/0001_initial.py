# Generated by Django 4.2.1 on 2023-05-09 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Hackathon",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "background_image",
                    models.ImageField(upload_to="media/background_images/"),
                ),
                (
                    "hackathon_image",
                    models.ImageField(upload_to="media/hackathon_images/"),
                ),
                (
                    "type_of_submission",
                    models.CharField(
                        choices=[
                            ("image", "Image"),
                            ("file", "File"),
                            ("link", "Link"),
                        ],
                        max_length=10,
                    ),
                ),
                ("start_datetime", models.DateTimeField()),
                ("end_datetime", models.DateTimeField()),
                ("reward_prize", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HackathonParticipant",
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
                ("submission_file", models.FileField(upload_to="media/submissions")),
                (
                    "hackathon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.hackathon"
                    ),
                ),
                (
                    "participant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.profile"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="hackathon",
            name="organizer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.profile"
            ),
        ),
    ]