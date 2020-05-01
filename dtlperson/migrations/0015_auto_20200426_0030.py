# Generated by Django 3.1 on 2020-04-26 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dtlperson', '0014_auto_20200425_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='dtlperson.address'),
        ),
    ]