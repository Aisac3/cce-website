# Generated by Django 3.2.13 on 2023-01-14 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0050_auto_20230114_0846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researchguides',
            name='department',
        ),
        migrations.RemoveField(
            model_name='researchguides',
            name='name',
        ),
        migrations.AddField(
            model_name='researchguides',
            name='faculty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.faculty'),
        ),
        migrations.AlterField(
            model_name='hero_image',
            name='page',
            field=models.CharField(choices=[('management', 'Management'), ('directors_desk', 'Directors Desk'), ('facilities', 'Facilities'), ('principals_desk', "Principal's Desk"), ('cce_in_media', 'CCE In Media'), ('governing_body', 'Governing Body'), ('organogram', 'Organogram'), ('mandatory_disclosure', 'Mandatory Disclosure'), ('antiraging_cell', 'AntiRaging Cell'), ('grivence_redressal_sysytem', 'Grivence Redressal System'), ('sc_st_monitoring_commite', 'Sc/St Monitoring Commitee'), ('iqac', 'IQAC'), ('examination_cell', 'Examination Cell'), ('PTA', 'PTA'), ('office', 'office'), ('nss', 'NSS'), ('college_union', 'College Union'), ('facilities', 'Facilities'), ('pta', 'PTA'), ('None', 'None'), ('research', 'Research'), ('arts', 'Arts'), ('sports', 'Sports')], default='None', max_length=200),
        ),
    ]
