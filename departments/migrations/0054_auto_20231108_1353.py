# Generated by Django 3.2.17 on 2023-11-08 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0053_alter_products_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
                ('url', models.URLField()),
                ('image', models.ImageField(blank=True, upload_to='alumni')),
                ('dep', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None')], default='None', max_length=200)),
            ],
            options={
                'verbose_name': 'Alumni',
                'verbose_name_plural': 'Alumnus',
            },
        ),
        migrations.RemoveField(
            model_name='holistics',
            name='link',
        ),
        migrations.RemoveField(
            model_name='holistics',
            name='type',
        ),
        migrations.RemoveField(
            model_name='social_activities',
            name='type',
        ),
        migrations.AddField(
            model_name='fdps',
            name='department',
            field=models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None')], default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='fdps',
            name='type',
            field=models.CharField(choices=[('attended', 'Attended'), ('organised', 'Organised')], default='attended', max_length=200),
        ),
        migrations.AlterField(
            model_name='fdps',
            name='duration',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='fdps',
            name='name',
            field=models.CharField(default='Everyone', max_length=200),
        ),
        migrations.AlterField(
            model_name='fdps',
            name='year',
            field=models.CharField(max_length=30),
        ),
    ]
