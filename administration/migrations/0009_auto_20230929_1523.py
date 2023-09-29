# Generated by Django 3.2.17 on 2023-09-29 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0008_auto_20230929_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='ptaexecutivecommitee',
            name='year',
            field=models.CharField(choices=[('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024')], default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='ptamembers',
            name='year',
            field=models.CharField(choices=[('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024')], default='none', max_length=20),
        ),
    ]
