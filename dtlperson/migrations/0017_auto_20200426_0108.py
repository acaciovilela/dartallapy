# Generated by Django 3.1 on 2020-04-26 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dtlperson', '0016_auto_20200426_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='person',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='dtlperson.person'),
        ),
    ]
