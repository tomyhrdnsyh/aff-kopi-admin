# Generated by Django 4.1.5 on 2023-01-16 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_order_producttype_products_orderdetails_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderdetails',
            options={'verbose_name_plural': 'Order details'},
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
