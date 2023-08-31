# Generated by Django 4.2.3 on 2023-08-31 23:45

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import django_resized.forms
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('link', models.CharField(default='', max_length=200)),
                ('appslink', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=100)),
                ('apartment_address', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zip', models.CharField(max_length=100)),
                ('address_type', models.CharField(choices=[('B', 'Billing'), ('S', 'Shipping')], max_length=1)),
                ('default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='AllProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='AllProductMainImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[150, 150], upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('slug', models.SlugField(unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shop.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('image', models.CharField(blank=True, max_length=240)),
                ('price', models.FloatField(blank=True, default=0)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('amount', models.IntegerField(default=5)),
                ('minamount', models.IntegerField(default=1)),
                ('variant', models.CharField(choices=[('None', 'None'), ('Size', 'Size'), ('Color', 'Color'), ('Size-Color', 'Size-Color')], default='None', max_length=10)),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image_detail', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('shipping_time', models.CharField(default='Shipping Times 5-7 days :)', max_length=100)),
                ('stock_status', models.CharField(default='In Stock', max_length=100)),
                ('cost_price', models.CharField(default='0', max_length=100)),
                ('sell_price', models.CharField(default='0', max_length=100)),
                ('product_status', models.CharField(default='This product available, Happy shopping :)', max_length=100)),
                ('note', models.CharField(default='This product available, Happy shopping :)', max_length=100)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('collection_details', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ManyToManyField(to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='LoginSecurity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('link', models.CharField(default='', max_length=200)),
                ('appslink', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='OrbitplugGuideline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('link', models.CharField(default='', max_length=200)),
                ('appslink', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(blank=True, max_length=20, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('order_code', models.CharField(default='None', max_length=20)),
                ('status', models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Preaparing', 'Preaparing'), ('OnShipping', 'OnShipping'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='New', max_length=20)),
                ('shiping_status', models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Preaparing', 'Preaparing'), ('OnShipping', 'OnShipping'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='New', max_length=20)),
                ('returns_status', models.CharField(choices=[('Apply', 'Apply'), ('Accepted', 'Accepted'), ('Preaparing', 'Preaparing'), ('OnShipping', 'OnShipping'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='Apply', max_length=20)),
                ('cancelled_status', models.CharField(choices=[('Apply', 'Apply'), ('Accepted', 'Accepted'), ('Preaparing', 'Preaparing'), ('OnShipping', 'OnShipping'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='Apply', max_length=20)),
                ('being_delivered', models.BooleanField(default=False)),
                ('received', models.BooleanField(default=False)),
                ('refund_requested', models.BooleanField(default=False)),
                ('refund_granted', models.BooleanField(default=False)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='shop.address')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.coupon')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='YourCanTryForSell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('link', models.CharField(default='', max_length=200)),
                ('appslink', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='YourOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('link', models.CharField(default='', max_length=200)),
                ('appslink', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='YourPayments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('link', models.CharField(default='', max_length=200)),
                ('appslink', models.CharField(default='', max_length=200)),
                ('phone', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='YourProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('link', models.CharField(default='', max_length=200)),
                ('appslink', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='None', max_length=100, null=True)),
                ('image_id', models.IntegerField(blank=True, default=0, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.color')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.size')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_customer_id', models.CharField(blank=True, max_length=50, null=True)),
                ('one_click_purchasing', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopping_fast_name', models.CharField(blank=True, max_length=50)),
                ('shopping_last_name', models.CharField(blank=True, max_length=50)),
                ('shopping_phone', models.CharField(blank=True, max_length=20)),
                ('shopping_address', models.CharField(blank=True, max_length=200)),
                ('shopping_district', models.CharField(blank=True, max_length=200)),
                ('shopping_division', models.CharField(blank=True, max_length=200)),
                ('shopping_zip_code', models.CharField(blank=True, max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('accepted', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('image', models.CharField(blank=True, max_length=240)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionID', models.CharField(blank=True, max_length=50)),
                ('taka', models.CharField(blank=True, max_length=4)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fast_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=11)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('district', models.CharField(blank=True, max_length=100)),
                ('division', models.CharField(blank=True, max_length=100)),
                ('zip_code', models.CharField(blank=True, max_length=20)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
                ('item_variations', models.ManyToManyField(to='shop.variants')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='shop.orderitem'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='shop.address'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='OderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=200)),
                ('orderid', models.CharField(default='None', max_length=200)),
                ('color', models.CharField(default='None', max_length=200)),
                ('size', models.CharField(default='None', max_length=200)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('amount', models.FloatField()),
                ('order_code', models.CharField(default='None', max_length=20)),
                ('status', models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Preaparing', 'Preaparing'), ('OnShipping', 'OnShipping'), ('Completed', 'Completed'), ('Return', 'Return'), ('Cencelled', 'Cencelled'), ('Delivered', 'Delivered')], default='New', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('shiping_status', models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Preaparing', 'Preaparing'), ('OnShipping', 'OnShipping'), ('Completed', 'Completed'), ('Cencelled', 'Cencelled')], default='New', max_length=20)),
                ('other_status', models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Preaparing', 'Preaparing'), ('OnShipping', 'OnShipping'), ('Completed', 'Completed'), ('Return', 'Return'), ('Cencelled', 'Cencelled'), ('Delivered', 'Delivered')], default='New', max_length=20)),
                ('returns_status', models.CharField(choices=[('Apply', 'Apply'), ('Accepted', 'Accepted'), ('Preaparing', 'Preaparing'), ('OnShipping', 'OnShipping'), ('Completed', 'Completed'), ('Cencelled', 'Cencelled')], default='Apply', max_length=20)),
                ('cancelled_status', models.CharField(choices=[('Apply', 'Apply'), ('Accepted', 'Accepted'), ('Preaparing', 'Preaparing'), ('OnShipping', 'OnShipping'), ('Completed', 'Completed'), ('Cencelled', 'Cencelled')], default='Apply', max_length=20)),
                ('returns_reason_sms', models.CharField(default='None', max_length=200)),
                ('cancelled_reason_sms', models.CharField(default='None', max_length=200)),
                ('user_returns_status', models.CharField(default='Apply', max_length=20)),
                ('user_cancelled_status', models.CharField(default='Apply', max_length=20)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('comment', models.CharField(blank=True, max_length=250)),
                ('rate', models.IntegerField(default=1)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BullingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fast_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('district', models.CharField(blank=True, max_length=200)),
                ('division', models.CharField(blank=True, max_length=200)),
                ('zip_code', models.CharField(blank=True, max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
