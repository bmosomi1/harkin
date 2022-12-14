# Generated by Django 3.1.5 on 2021-10-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0029_watersysconf_update_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterSysConfHist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standing_charge', models.FloatField(max_length=250, null=True)),
                ('rate', models.FloatField(max_length=250, null=True)),
                ('comment', models.CharField(default=0, max_length=250, null=True)),
                ('account_number', models.CharField(max_length=250)),
                ('processed', models.IntegerField(max_length=250, null=True)),
                ('reading_type', models.CharField(max_length=250, null=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'water_sys_config_hist',
                'verbose_name_plural': 'water_sys_config_hist',
            },
        ),
    ]
