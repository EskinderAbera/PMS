# Generated by Django 4.1 on 2022-10-21 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsc', '0002_kpi_kpi_q1_kpi_kpi_q2_kpi_kpi_q3_kpi_kpi_q4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='kpi_q1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='kpi_q2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='kpi_q3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='kpi_q4',
            field=models.IntegerField(default=0),
        ),
    ]
