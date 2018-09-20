# Generated by Django 2.0.7 on 2018-09-09 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazingQuote', '0003_auto_20180909_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazingquotesabout',
            name='tagline',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='product',
            name='type_of_product',
            field=models.CharField(choices=[('BAND', 'Wrist band'), ('TSHIRT', 'T-shirt'), ('BOOK', 'Book'), ('CUP', 'Cup')], max_length=64, verbose_name='Product Type'),
        ),
        migrations.AlterField(
            model_name='trainingtopic',
            name='category',
            field=models.CharField(choices=[('ENTREPRENEURSHIP', 'Entrepreneurship'), ('LIFE COACHING', 'Life Coaching'), ('LEADERSHIP', 'Leadership'), ('RELATIONSHIP', 'Relationship')], default='LIFE COACHING', max_length=20),
        ),
    ]