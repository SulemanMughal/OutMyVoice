# Generated by Django 2.2.12 on 2020-05-06 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0020_auto_20200506_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='Banner/%y/%m/%d/', verbose_name='Banner')),
            ],
        ),
    ]