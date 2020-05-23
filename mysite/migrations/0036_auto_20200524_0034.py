# Generated by Django 2.2.12 on 2020-05-23 19:34

from django.db import migrations, models
import mysite.models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0035_auto_20200510_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, verbose_name='Member Name')),
                ('description', models.TextField(default=None, max_length=500, verbose_name='Member Desciption')),
                ('gAdmin', models.CharField(choices=[('True', 'Yes'), ('False', 'No'), ('None', 'None')], default='None', max_length=10, null=True, verbose_name='Global Admin')),
                ('cAdmin', models.CharField(choices=[('Nigeria', 'Nigeria'), ('Abuja', 'Abuja'), ('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Cross River', 'Cross River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Enugu', 'Enugu'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara'), ('National Coverage', 'National Coverage'), ('None', 'None')], default=None, max_length=100, null=True, verbose_name='Coverage Admin')),
                ('iProfile', models.ImageField(upload_to='Team/Images/%y/%m/%d/', validators=[mysite.models.validate_image], verbose_name='Staff Member Profile Image')),
            ],
        ),
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.AlterField(
            model_name='webbanner',
            name='banner',
            field=models.ImageField(upload_to='Banner/%y/%m/%d/', validators=[mysite.models.validate_image], verbose_name='Banner'),
        ),
    ]
