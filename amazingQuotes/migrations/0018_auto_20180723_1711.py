# Generated by Django 2.0.7 on 2018-07-23 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazingQuotes', '0017_auto_20180723_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type_of_product',
            field=models.CharField(choices=[('BOOK', 'Book'), ('TSHIRT', 'T-shirt'), ('BAND', 'Wrist band'), ('CUP', 'Cup')], max_length=64, verbose_name='Product Type'),
        ),
        migrations.AlterField(
            model_name='value',
            name='description',
            field=models.TextField(max_length=256, verbose_name='Value Description'),
        ),
    ]
