# Generated by Django 2.2.12 on 2020-04-21 21:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_auto_20200422_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition_signer',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Commendation_Signer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Reason', models.TextField(blank=True)),
                ('show_comment', models.BooleanField(blank=True, default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('commendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Commendation')),
            ],
        ),
    ]
