from django.urls import path
from . import views

urlpatterns = [
    path("get_provider", views.get_provider, name="get_provider"),
    path("", views.def_phone_provider_form, name="def_phone_provider_form"),
]
