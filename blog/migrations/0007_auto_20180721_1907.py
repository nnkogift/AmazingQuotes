# Generated by Django 2.0.6 on 2018-07-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180720_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('ENTREPRENEURSHIP', 'Entrepreneurship'), ('LEADERSHIP', 'Leadership'), ('RELATIONSHIP', 'Relationship'), ('LIFE COACHING', 'Life Coaching')], default='LIFE', max_length=64, verbose_name='Post Category'),
        ),
    ]
