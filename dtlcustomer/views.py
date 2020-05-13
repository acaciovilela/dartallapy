from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

def index(request):
    customers = Customer.objects.all()
    return render(request, 'customer/index.html', {'customers': customers})

def add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer')
    else:
        form = CustomerForm()
    return render(request, 'customer/add.html', {'form': form})
