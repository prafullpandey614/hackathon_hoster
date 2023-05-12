# Generated by Django 4.2.1 on 2023-05-12 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_hackathon_end_datetime_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hackathonparticipant",
            name="submission_file",
        ),
        migrations.CreateModel(
            name="Submission",
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
                    "file",
                    models.FileField(
                        blank=True, null=True, upload_to="media/submission_files/"
                    ),
                ),
                (
                    "link_submission",
                    models.URLField(
                        blank=True, default="https://example.com", null=True
                    ),
                ),
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
    ]