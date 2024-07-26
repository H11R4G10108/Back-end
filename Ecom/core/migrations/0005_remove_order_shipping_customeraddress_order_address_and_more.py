# Generated by Django 5.0.3 on 2024-07-04 11:24

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_orderdetail_quantity_alter_product_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipping',
        ),
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('addressID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_phonenumber', message='Enter a valid phone number.', regex='(03|05|07|08|09|01[2|6|8|9])+([0-9]{8})\\b')])),
                ('city', models.CharField(max_length=64)),
                ('street', models.CharField(max_length=64)),
                ('default', models.BooleanField()),
                ('user', models.ForeignKey(help_text='The user of the shipping information.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(default=1, help_text='The shipping ìnformation of the order', on_delete=django.db.models.deletion.CASCADE, to='core.customeraddress'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ShippingInfor',
        ),
    ]