# Generated by Django 2.2.20 on 2023-08-11 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0104_challenge_evaluation_module_error"),
    ]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="has_prize",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="challenge",
            name="has_sponsors",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="ChallengeSponsor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("website", models.URLField(blank=True, null=True)),
                (
                    "challenge",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="challenges.Challenge",
                    ),
                ),
            ],
            options={
                "db_table": "challenge_sponsor",
            },
        ),
        migrations.CreateModel(
            name="ChallengePrize",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("amount", models.CharField(max_length=10)),
                (
                    "description",
                    models.CharField(blank=True, max_length=25, null=True),
                ),
                ("rank", models.PositiveIntegerField()),
                (
                    "challenge",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="challenges.Challenge",
                    ),
                ),
            ],
            options={
                "db_table": "challenge_prize",
            },
        ),
    ]
