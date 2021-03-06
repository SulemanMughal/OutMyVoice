# Generated by Django 2.2.12 on 2020-05-10 11:35

from django.db import migrations, models
import mysite.models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0031_auto_20200510_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='iProfile',
            field=models.ImageField(upload_to='Team/Images/%y/%m/%d/', validators=[mysite.models.validate_image], verbose_name='Team Member Profile Image'),
        ),
        migrations.AlterField(
            model_name='webbanner',
            name='banner',
            field=models.ImageField(upload_to='Banner/%y/%m/%d/', validators=[mysite.models.validate_image], verbose_name='Banner'),
        ),
    ]
