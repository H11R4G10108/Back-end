# Generated by Django 5.0.3 on 2024-07-09 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_order_subtotal_alter_order_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_fee',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=65),
        ),
    ]