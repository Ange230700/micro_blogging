# Generated by Django 5.2 on 2025-04-18 17:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Session",
            fields=[
                ("session_id", models.AutoField(primary_key=True, serialize=False)),
                ("token", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("expires_at", models.DateTimeField()),
            ],
        ),
    ]
