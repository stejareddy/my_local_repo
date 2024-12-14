import socket
from django.shortcuts import render

def dns_lookup(request):
    ip_address = None
    error_message = None

    if request.method == "POST":
        domain = request.POST.get("domain")
        try:
            # Perform DNS lookup
            ip_address = socket.gethostbyname(domain)
        except socket.gaierror:
            error_message = f"Unable to resolve IP for domain: {domain}"

    return render(request, "dns_lookup.html", {"ip_address": ip_address, "error_message": error_message})
