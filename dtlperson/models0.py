#
# import datetime
# from django.db import models
#
# class Person(models.Model):
#     name = models.CharField("Nome", max_length=255)
#     document = models.CharField("CPF/CNPJ", max_length=255)
#     register_date = models.DateTimeField("Data de Cadastro", auto_now=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = "Pessoa"
#         ordering = ['name']
#
# class Address(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
#     address = models.CharField("Endereço", max_length=255)
#     number = models.IntegerField("Número")
#     complement = models.CharField("Complemento", max_length=255)
#     quarter = models.CharField("Bairro", max_length=255)
#     postal_code = models.CharField("CEP", max_length=255)
#     city = models.CharField("Cidade", max_length=255)
#     state = models.CharField("Estado", max_length=255)
#     country = models.CharField("Pais", max_length=255)
#     class Meta:
#         verbose_name = "Endereço"
#
# class Contact(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
#     email = models.EmailField("E-mail")
#     site = models.CharField("Site", max_length=255)
#     phone = models.CharField("Telefone", max_length=255)
#     cell = models.CharField("Celular", max_length=255)
#     class Meta:
#         verbose_name = "Contato"
#
# class Customer(Person):
#     class Meta:
#         verbose_name = "Cliente"
#         verbose_name_plural = "Clientes"
#
# class Supplier(Person):
#     class Meta:
#         verbose_name = "Fornecedor"
#         verbose_name_plural = "Fornecedores"
