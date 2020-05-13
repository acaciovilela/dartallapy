from django.db import models
from dtlperson.models import Person

class Customer(Person):
    def __str__(parent):
        return parent.name

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
