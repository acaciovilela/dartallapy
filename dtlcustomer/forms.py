from dtlperson.forms import PersonForm
from django import forms
from .models import Customer

class CustomerForm(PersonForm):
    class Meta:
        model = Customer
        fields = '__all__'
