from django.urls import path, include
from . import views

app_name = 'person'

urlpatterns = [
    path('customer/', include('customer.urls'))
]
