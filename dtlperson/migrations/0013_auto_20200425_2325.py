# Generated by Django 3.1 on 2020-04-26 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtlperson', '0012_auto_20200425_2309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='person',
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={},
        ),
        migrations.RemoveField(
            model_name='person',
            name='document',
        ),
        migrations.RemoveField(
            model_name='person',
            name='register_date',
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
