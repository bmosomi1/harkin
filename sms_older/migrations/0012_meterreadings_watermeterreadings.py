# Generated by Django 3.1.5 on 2021-09-09 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0011_auto_20210909_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeterReadings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=250)),
                ('msisdn', models.CharField(max_length=250)),
                ('account_number', models.CharField(max_length=250)),
                ('id_num', models.CharField(max_length=250, null=True)),
                ('meter_num', models.CharField(max_length=250, null=True)),
                ('customer_rate', models.CharField(max_length=250, null=True)),
                ('reading_type', models.CharField(max_length=250, null=True)),
                ('last_meter_reading_date', models.CharField(max_length=250, null=True)),
                ('comment', models.EmailField(max_length=250, null=True)),
                ('court', models.CharField(max_length=250, null=True)),
                ('network', models.CharField(max_length=250, null=True)),
                ('previous_reading', models.FloatField(default=0, max_length=250, null=True)),
                ('readings', models.FloatField(default=0, max_length=250, null=True)),
                ('amount_from_units', models.FloatField(default=0, max_length=250, null=True)),
                ('credit', models.FloatField(default=0, max_length=250, null=True)),
                ('arrears', models.FloatField(default=0, max_length=250, null=True)),
                ('amount_due', models.FloatField(default=0, max_length=250, null=True)),
                ('payable', models.FloatField(default=0, max_length=250, null=True)),
                ('confirmed', models.IntegerField(default=0, max_length=250, null=True)),
                ('processed', models.IntegerField(default=0, max_length=250, null=True)),
                ('message', models.IntegerField(default=0, max_length=250, null=True)),
                ('units_consumed', models.FloatField(default=0, max_length=250, null=True)),
                ('last_payment_date', models.CharField(max_length=250, null=True)),
                ('meter_change_date', models.CharField(max_length=250, null=True)),
                ('connection_fee_paid', models.FloatField(default=0, max_length=250, null=True)),
                ('read_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'water_meterreading',
                'verbose_name_plural': 'water_meterreadings',
            },
        ),
        migrations.CreateModel(
            name='WaterMeterReadings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=250)),
                ('msisdn', models.CharField(max_length=250)),
                ('account_number', models.CharField(max_length=250)),
                ('id_num', models.CharField(max_length=250, null=True)),
                ('meter_num', models.CharField(max_length=250, null=True)),
                ('customer_rate', models.CharField(max_length=250, null=True)),
                ('reading_type', models.CharField(max_length=250, null=True)),
                ('last_meter_reading_date', models.CharField(max_length=250, null=True)),
                ('comment', models.EmailField(max_length=250, null=True)),
                ('court', models.CharField(max_length=250, null=True)),
                ('network', models.CharField(max_length=250, null=True)),
                ('previous_reading', models.FloatField(default=0, max_length=250, null=True)),
                ('readings', models.FloatField(default=0, max_length=250, null=True)),
                ('amount_from_units', models.FloatField(default=0, max_length=250, null=True)),
                ('credit', models.FloatField(default=0, max_length=250, null=True)),
                ('arrears', models.FloatField(default=0, max_length=250, null=True)),
                ('amount_due', models.FloatField(default=0, max_length=250, null=True)),
                ('payable', models.FloatField(default=0, max_length=250, null=True)),
                ('confirmed', models.IntegerField(default=0, max_length=250, null=True)),
                ('processed', models.IntegerField(default=0, max_length=250, null=True)),
                ('message', models.IntegerField(default=0, max_length=250, null=True)),
                ('units_consumed', models.FloatField(default=0, max_length=250, null=True)),
                ('last_payment_date', models.CharField(max_length=250, null=True)),
                ('meter_change_date', models.CharField(max_length=250, null=True)),
                ('connection_fee_paid', models.FloatField(default=0, max_length=250, null=True)),
                ('read_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'water_meterreading',
                'verbose_name_plural': 'water_meterreadings',
            },
        ),
    ]
