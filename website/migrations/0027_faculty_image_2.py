# Generated by Django 3.2.13 on 2022-11-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_auto_20221111_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='image_2',
            field=models.ImageField(default='faculty.jpeg', upload_to='faculty'),
        ),
    ]
