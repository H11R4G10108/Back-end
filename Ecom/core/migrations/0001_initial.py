# Generated by Django 5.0.6 on 2024-05-24 03:54

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('catID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50, verbose_name="The product's category")),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('sizeID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('Free Size', 'Free Size')], max_length=10, verbose_name="The product's size")),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('statusID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Shipping', 'Shipping'), ('Delivered', 'Delivered')], default='Pending', max_length=20, verbose_name="The order's status")),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Username', max_length=10)),
                ('email', models.EmailField(help_text="The User's email address.", max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('date_order', models.DateTimeField(default=django.utils.timezone.now)),
                ('shipping_fee', models.DecimalField(decimal_places=2, max_digits=65)),
                ('total_shipping', models.DecimalField(decimal_places=2, max_digits=65)),
                ('user', models.ForeignKey(help_text='The user of the order', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=65)),
                ('price_discounted', models.DecimalField(decimal_places=2, default=0, max_digits=65, null=True)),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(default='default.jpg', null=True, upload_to='product_image/', verbose_name="The product's image")),
                ('description', models.TextField(null=True)),
                ('category', models.ForeignKey(help_text='The category of the product', on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('size', models.ForeignKey(help_text='The size of the product', on_delete=django.db.models.deletion.CASCADE, to='core.size')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('detailID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('total', models.DecimalField(decimal_places=2, max_digits=65)),
                ('order', models.ForeignKey(help_text='The order that the detail belongs to', on_delete=django.db.models.deletion.CASCADE, to='core.order')),
                ('product', models.ForeignKey(help_text='The product in the detail', on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('reviewID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('review', models.TextField(null=True)),
                ('date_review', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(help_text='The promotion for the product', on_delete=django.db.models.deletion.CASCADE, to='core.product')),
                ('user', models.ForeignKey(help_text='The user of the shipping information', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('promoID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=65)),
                ('type', models.BooleanField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('description', models.TextField(null=True)),
                ('product', models.ForeignKey(help_text='The promotion for the product', on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingInfor',
            fields=[
                ('shipID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('tel', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('city', models.CharField(max_length=64)),
                ('street', models.CharField(max_length=64)),
                ('status', models.BooleanField()),
                ('user', models.ForeignKey(help_text='The user of the shipping information.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.ForeignKey(help_text='The shipping ìnformation of the order', on_delete=django.db.models.deletion.CASCADE, to='core.shippinginfor'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(help_text='The status of the order', on_delete=django.db.models.deletion.CASCADE, to='core.status'),
        ),
    ]
