# Generated by Django 4.2.8 on 2023-12-23 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('founding_date', models.DateField()),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hw.genre')),
            ],
        ),
    ]
