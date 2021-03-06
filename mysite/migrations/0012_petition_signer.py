# Generated by Django 2.2.12 on 2020-04-21 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_delete_approvedmanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Petition_Signer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100, unique=True)),
                ('Reason', models.TextField(blank=True)),
                ('show_comment', models.BooleanField(blank=True, default=True)),
                ('petition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Petition')),
            ],
        ),
    ]
