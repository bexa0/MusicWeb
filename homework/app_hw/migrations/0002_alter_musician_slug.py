# Generated by Django 4.2.8 on 2023-12-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hw', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
