# Generated by Django 2.2.12 on 2020-04-20 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_userprofile_golbal_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='petitionresponsefeedback',
            name='response',
            field=models.CharField(choices=[(True, 'Yes'), (False, 'No')], default=False, max_length=3),
        ),
    ]
