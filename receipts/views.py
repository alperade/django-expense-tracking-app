from django.shortcuts import render
from receipts.models import Receipt


def ReceiptListView(request):
    context = {"receipts": Receipt.objects.all()}

    return render(request, "receipts/list.html", context)
