# Generated by Django 3.0.5 on 2020-04-27 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtluser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
