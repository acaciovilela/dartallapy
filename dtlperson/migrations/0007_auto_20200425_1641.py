# Generated by Django 3.1 on 2020-04-25 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dtlperson', '0006_contact_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dtlperson.person')),
            ],
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Endereço'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contato'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['name'], 'verbose_name': 'Pessoa'},
        ),
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=255, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='address',
            name='complement',
            field=models.CharField(max_length=255, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=255, verbose_name='Pais'),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.IntegerField(verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(max_length=255, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='address',
            name='quarter',
            field=models.CharField(max_length=255, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=255, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cell',
            field=models.CharField(max_length=255, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=255, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='site',
            field=models.CharField(max_length=255, verbose_name='Site'),
        ),
        migrations.AlterField(
            model_name='person',
            name='document',
            field=models.CharField(max_length=255, verbose_name='CPF/CNPJ'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='person',
            name='register_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de Cadastro'),
        ),
    ]