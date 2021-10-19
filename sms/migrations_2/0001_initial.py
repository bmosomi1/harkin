# Generated by Django 2.2.4 on 2019-09-30 07:07

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('location', models.CharField(max_length=250, null=True)),
                ('phone_number', models.TextField(null=True)),
                ('access_code', models.CharField(default='711037', max_length=11)),
                ('service_id', models.CharField(default='6015152000175328', max_length=50)),
                ('business_name', models.CharField(default='Business Name', max_length=100)),
                ('credit', models.IntegerField(default=5)),
                ('customer_code', models.IntegerField(null=True)),
                ('sender_name', models.CharField(default='Roberms LTD', max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='OutgoingDone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.BigIntegerField()),
                ('service_id', models.CharField(default='68124233232', max_length=50)),
                ('access_code', models.CharField(default='72345', max_length=50)),
                ('phone_number', models.TextField(null=True)),
                ('text_message', models.TextField(max_length=600, null=True)),
                ('track_code', models.CharField(max_length=50, null=True)),
                ('sent_time', models.DateTimeField(auto_now_add=True)),
                ('delivery_status', models.CharField(max_length=1000, null=True)),
                ('oc', models.IntegerField(max_length=11, null=True)),
                ('code', models.IntegerField(null=True)),
                ('request_identifier', models.CharField(max_length=3000, null=True)),
                ('extra_status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'OutgoingDone',
                'verbose_name_plural': 'OutgoingsDone',
            },
        ),
        migrations.CreateModel(
            name='SalesPerson',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.IntegerField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Sms_TopUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_phone', models.CharField(max_length=250)),
                ('transaction_ref', models.CharField(max_length=250)),
                ('amount', models.CharField(max_length=250)),
                ('till_number', models.CharField(max_length=250)),
                ('f_name', models.CharField(max_length=250)),
                ('l_name', models.CharField(max_length=250)),
                ('signature', models.CharField(max_length=250)),
                ('account_no', models.CharField(max_length=250)),
                ('transaction_type', models.CharField(max_length=250)),
                ('verifycode', models.CharField(max_length=250)),
                ('user_id', models.IntegerField()),
                ('verified', models.IntegerField(default=0)),
                ('timestamp', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='UserTopUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone_number', models.CharField(max_length=12)),
                ('transaction_ref', models.IntegerField()),
                ('amount', models.FloatField()),
                ('till_number', models.IntegerField()),
                ('f_name', models.CharField(max_length=250)),
                ('l_name', models.CharField(max_length=250)),
                ('verify_code', models.IntegerField()),
                ('user_id', models.IntegerField(null=True)),
                ('verified', models.BooleanField(default=False)),
                ('timestamp', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Customer')),
                ('sales_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.SalesPerson')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Outgoing2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(default='68124233232', max_length=50)),
                ('access_code', models.CharField(default='72345', max_length=50)),
                ('phone_number', models.TextField(null=True)),
                ('text_message', models.TextField(max_length=600, null=True)),
                ('track_code', models.CharField(max_length=50, null=True)),
                ('sent_time', models.DateTimeField(auto_now_add=True)),
                ('delivery_status', models.CharField(max_length=1000, null=True)),
                ('oc', models.IntegerField(max_length=11, null=True)),
                ('code', models.IntegerField(null=True)),
                ('request_identifier', models.CharField(max_length=3000, null=True)),
                ('extra_status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Customer')),
            ],
            options={
                'verbose_name': 'Outgoing2',
                'verbose_name_plural': 'Outgoings2',
            },
        ),
        migrations.CreateModel(
            name='Outgoing1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(max_length=50)),
                ('access_code', models.CharField(max_length=50)),
                ('phone_number', models.TextField(null=True)),
                ('text_message', models.TextField(max_length=600, null=True)),
                ('track_code', models.CharField(max_length=50, null=True)),
                ('sent_time', models.DateTimeField(auto_now_add=True)),
                ('delivery_status', models.CharField(max_length=1000, null=True)),
                ('oc', models.IntegerField(max_length=11, null=True)),
                ('code', models.IntegerField(null=True)),
                ('request_identifier', models.CharField(max_length=3000, null=True)),
                ('extra_status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Customer')),
            ],
            options={
                'verbose_name': 'Outgoing1',
                'verbose_name_plural': 'Outgoing1',
            },
        ),
        migrations.CreateModel(
            name='Outgoing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(default='68124233232', max_length=50)),
                ('access_code', models.CharField(default='72345', max_length=50)),
                ('phone_number', models.TextField(null=True)),
                ('text_message', models.TextField(max_length=600, null=True)),
                ('track_code', models.CharField(max_length=50, null=True)),
                ('sent_time', models.DateTimeField(auto_now_add=True)),
                ('delivery_status', models.CharField(max_length=1000, null=True)),
                ('oc', models.IntegerField(max_length=11, null=True)),
                ('code', models.IntegerField(null=True)),
                ('request_identifier', models.CharField(max_length=3000, null=True)),
                ('extra_status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Customer')),
            ],
            options={
                'verbose_name': 'Outgoing',
                'verbose_name_plural': 'Outgoings',
            },
        ),
        migrations.CreateModel(
            name='MpesaPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone_number', models.IntegerField()),
                ('reference_number', models.CharField(max_length=250)),
                ('amount', models.FloatField()),
                ('till_number', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('verified', models.BooleanField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Customer')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250, null=True)),
                ('phone_number', models.CharField(max_length=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Group')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]