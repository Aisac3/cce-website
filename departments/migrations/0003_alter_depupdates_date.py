# Generated by Django 3.2.13 on 2022-11-29 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_depupdates_mission_poes_pos_psos_vission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depupdates',
            name='date',
            field=models.DateField(),
        ),
    ]
