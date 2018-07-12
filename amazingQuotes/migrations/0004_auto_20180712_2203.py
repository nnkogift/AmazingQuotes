# Generated by Django 2.0.7 on 2018-07-12 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazingQuotes', '0003_auto_20180712_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazingquotesabout',
            name='email',
            field=models.EmailField(default='amazingquotes@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='amazingquotesabout',
            name='facebook',
            field=models.URLField(default='https://facebook.com/amazingquotes', max_length=128, verbose_name='Facebook link'),
        ),
        migrations.AddField(
            model_name='amazingquotesabout',
            name='instagram',
            field=models.URLField(default='https://insta.com/amazingquotes', max_length=128, verbose_name='Instagram link'),
        ),
        migrations.AddField(
            model_name='amazingquotesabout',
            name='linkedin',
            field=models.CharField(default='https://linkedin.com/amazingquotes', max_length=128, verbose_name='Linkedin link'),
        ),
        migrations.AddField(
            model_name='amazingquotesabout',
            name='phone_no',
            field=models.CharField(default='0712626160', max_length=20),
        ),
        migrations.AddField(
            model_name='amazingquotesabout',
            name='twitter',
            field=models.URLField(default='https://twitter.com/amazingquotes', max_length=128, verbose_name='Twitter link'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type_of_product',
            field=models.CharField(choices=[('TSHIRT', 'T-shirt'), ('CUP', 'Cup'), ('BAND', 'Wrist band'), ('BOOK', 'Available')], max_length=64, verbose_name='Product Type'),
        ),
    ]