# Generated by Django 2.0.7 on 2018-08-10 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazingQuote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='product',
            name='feature',
            field=models.CharField(choices=[('NO', 'No'), ('YES', 'Yes')], default='YES', max_length=10, verbose_name='Is it Featured?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type_of_product',
            field=models.CharField(choices=[('BOOK', 'Book'), ('CUP', 'Cup'), ('BAND', 'Wrist band'), ('TSHIRT', 'T-shirt')], max_length=64, verbose_name='Product Type'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='speaker',
            field=models.CharField(choices=[('NO', 'No'), ('YES', 'Yes')], default='NO', max_length=5),
        ),
        migrations.AlterField(
            model_name='trainingtopic',
            name='category',
            field=models.CharField(choices=[('LEADERSHIP', 'Leadership'), ('LIFE COACHING', 'Life Coaching'), ('ENTREPRENEURSHIP', 'Entrepreneurship'), ('RELATIONSHIP', 'Relationship')], default='LIFE COACHING', max_length=20),
        ),
    ]
