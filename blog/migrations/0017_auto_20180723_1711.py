# Generated by Django 2.0.7 on 2018-07-23 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20180723_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('RELATIONSHIP', 'Relationship'), ('LEADERSHIP', 'Leadership'), ('ENTREPRENEURSHIP', 'Entrepreneurship'), ('LIFE COACHING', 'Life Coaching')], default='LIFE', max_length=64, verbose_name='Post Category'),
        ),
    ]
