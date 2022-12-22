# Generated by Django 3.2.13 on 2022-12-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0037_alter_upcomingevents_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='type',
            field=models.CharField(choices=[('img', 'IMAGE'), ('vdo', 'VIDEO')], default='img', max_length=200),
        ),
        migrations.AddField(
            model_name='gallery',
            name='video',
            field=models.FileField(blank=True, upload_to='Heros_Videos'),
        ),
    ]
