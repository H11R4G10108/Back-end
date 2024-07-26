# Generated by Django 5.0.3 on 2024-06-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]