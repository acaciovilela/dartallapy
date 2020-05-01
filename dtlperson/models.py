import datetime
from django.db import models

class Person(models.Model):
    name = models.CharField("Nome", max_length=255)
    document = models.CharField("CPF/CNPJ", max_length=255, null=True)
    register_date = models.DateTimeField("Data de Cadastro", auto_now=True)

class Address(models.Model):
    name = models.CharField("Endereço", max_length=255)
    number = models.IntegerField("Número", null=True)
    complement = models.CharField("Complemento", max_length=255, null=True)
    quarter = models.CharField("Bairro", max_length=255, null=True)
    postal_code = models.CharField("CEP", max_length=255, null=True)
    city = models.CharField("Cidade", max_length=255, null=True)
    state = models.CharField("Estado", max_length=255, null=True)
    country = models.CharField("Pais", max_length=255, null=True)
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        parent_link=True,
        null=True,
        unique=True,
    )
    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

class Contact(models.Model):
    email = models.EmailField("E-mail", null=True)
    site = models.CharField("Site", max_length=255, null=True)
    phone = models.CharField("Telefone", max_length=255, null=True)
    cell = models.CharField("Celular", max_length=255, null=True)
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        parent_link=True,
        null=True,
        unique=True,
    )
    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

class Customer(Person):
    def __str__(parent):
        return parent.name
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Supplier(Person):
    def __str__(parent):
        return parent.name
    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
