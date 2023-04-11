# Generated by Django 3.2.17 on 2023-04-11 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placements', '0008_placementfaculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacementGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='gallery')),
                ('video', models.FileField(blank=True, upload_to='PlacementGallery')),
                ('type', models.CharField(choices=[('img', 'IMAGE'), ('vdo', 'VIDEO')], default='img', max_length=200)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='PlacementStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graph', models.ImageField(upload_to=None, verbose_name='Graph')),
            ],
        ),
    ]
