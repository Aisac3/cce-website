# Generated by Django 3.2.13 on 2023-01-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0052_facultystudentpublications'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='investor',
            field=models.CharField(default='', max_length=500, verbose_name='Name of Investor'),
        ),
        migrations.AlterField(
            model_name='facultystudentpublications',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
