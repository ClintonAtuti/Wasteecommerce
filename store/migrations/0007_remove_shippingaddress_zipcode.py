# Generated by Django 4.1.1 on 2022-10-30 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='zipcode',
        ),
    ]
