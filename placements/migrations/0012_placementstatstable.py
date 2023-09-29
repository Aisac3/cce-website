# Generated by Django 3.2.17 on 2023-09-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placements', '0011_alter_placementfaculty_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacementStatsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024')], default='None', max_length=30)),
                ('students', models.IntegerField()),
                ('placement', models.IntegerField()),
                ('higher_studies', models.IntegerField()),
                ('total', models.IntegerField()),
                ('highest', models.IntegerField()),
                ('avg', models.IntegerField()),
            ],
        ),
    ]
