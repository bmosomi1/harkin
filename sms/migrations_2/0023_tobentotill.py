# Generated by Django 2.2.4 on 2020-01-28 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0022_auto_20200127_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='TobentoTill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_number', models.IntegerField()),
                ('till_name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('till_number', models.IntegerField()),
            ],
        ),
    ]
