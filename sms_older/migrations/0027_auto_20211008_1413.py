# Generated by Django 3.1.5 on 2021-10-08 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0026_auto_20211008_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watersysconf',
            old_name='read_date',
            new_name='add_date',
        ),
        migrations.RenameField(
            model_name='watersysconf',
            old_name='readings',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='watersysconf',
            name='msisdn',
        ),
        migrations.RemoveField(
            model_name='watersysconf',
            name='names',
        ),
        migrations.AddField(
            model_name='watersysconf',
            name='rate',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='watersysconf',
            name='standing_charge',
            field=models.CharField(max_length=250, null=True),
        ),
    ]