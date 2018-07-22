# Generated by Django 2.0.7 on 2018-07-17 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazingQuotes', '0004_auto_20180712_2203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amazingquotesabout',
            options={'verbose_name': 'About Amazing Quotes', 'verbose_name_plural': 'About Amazing Quotes'},
        ),
        migrations.AlterField(
            model_name='product',
            name='type_of_product',
            field=models.CharField(choices=[('BOOK', 'Available'), ('CUP', 'Cup'), ('BAND', 'Wrist band'), ('TSHIRT', 'T-shirt')], max_length=64, verbose_name='Product Type'),
        ),
    ]
