
from django.urls import path
from . import views

urlpatterns = [
    path('get_provider', views.get_provider, name='def_number'),
    path('', views.def_phone_provider_form)
]