# Generated by Django 2.2.12 on 2020-05-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0023_auto_20200506_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webbanner',
            name='banner',
            field=models.ImageField(height_field=350, upload_to='Banner/%y/%m/%d/', verbose_name='Banner', width_field=1920),
        ),
    ]