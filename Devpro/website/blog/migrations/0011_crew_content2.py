# Generated by Django 4.2.11 on 2024-04-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_crew'),
    ]

    operations = [
        migrations.AddField(
            model_name='crew',
            name='content2',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
