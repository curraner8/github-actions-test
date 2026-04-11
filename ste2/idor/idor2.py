from django.db import models
from django.http import JsonResponse

def get_invoice(request):
    # VULNERABLE: WHERE clause uses user-supplied invoice_id without ownership check
    invoice_id = request.GET.get('invoice_id')
    invoice = Invoices.objects.raw(
        f"SELECT * FROM invoices_invoices WHERE id = {invoice_id}"
    )
    # No check that invoice belongs to request.user
    return JsonResponse({'invoice': invoice[0].__dict__})

# SOURCE: https://github.com/OWASP/railsgoat/wiki/
