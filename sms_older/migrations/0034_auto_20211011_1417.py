# Generated by Django 3.1.5 on 2021-10-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0033_auto_20211011_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watersmsout',
            name='court',
            field=models.CharField(default=0, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='watersmsout',
            name='network',
            field=models.CharField(default=0, max_length=400, null=True),
        ),
    ]
