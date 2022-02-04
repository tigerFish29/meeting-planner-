# Generated by Django 4.0.2 on 2022-02-04 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_meeting_duration_meeting_start_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('floorNumber', models.IntegerField()),
                ('roomNumber', models.IntegerField()),
            ],
        ),
    ]