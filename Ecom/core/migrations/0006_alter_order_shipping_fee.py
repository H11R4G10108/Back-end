# Generated by Django 5.0.3 on 2024-07-07 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_order_shipping_customeraddress_order_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_fee',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=65),
        ),
    ]
