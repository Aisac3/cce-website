# Generated by Django 3.2.17 on 2023-11-07 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0049_higher_holistics_placements_social_activities'),
    ]

    operations = [
        migrations.AddField(
            model_name='dabtable',
            name='priority',
            field=models.IntegerField(default=10),
        ),
    ]
