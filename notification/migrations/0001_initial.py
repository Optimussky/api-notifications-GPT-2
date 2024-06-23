# Generated by Django 5.0 on 2024-06-22 22:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('body', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
