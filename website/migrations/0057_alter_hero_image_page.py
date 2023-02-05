# Generated by Django 3.2.13 on 2023-02-02 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0056_gallery_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero_image',
            name='page',
            field=models.CharField(choices=[('management', 'Management'), ('directors_desk', 'Directors Desk'), ('facilities', 'Facilities'), ('principals_desk', "Principal's Desk"), ('cce_in_media', 'CCE In Media'), ('governing_body', 'Governing Body'), ('organogram', 'Organogram'), ('mandatory_disclosure', 'Mandatory Disclosure'), ('antiraging_cell', 'AntiRaging Cell'), ('grivence_redressal_sysytem', 'Grivence Redressal System'), ('sc_st_monitoring_commite', 'Sc/St Monitoring Commitee'), ('iqac', 'IQAC'), ('examination_cell', 'Examination Cell'), ('PTA', 'PTA'), ('office', 'office'), ('nss', 'NSS'), ('college_union', 'College Union'), ('facilities', 'Facilities'), ('pta', 'PTA'), ('None', 'None'), ('research', 'Research'), ('arts', 'Arts'), ('sports', 'Sports'), ('placements', 'Placements')], default='None', max_length=200),
        ),
    ]
