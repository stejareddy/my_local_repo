from django.urls import path
from dns_lookup.views import dns_lookup

urlpatterns = [
    path('dns_lookup/', dns_lookup, name='dns_lookup')
]
