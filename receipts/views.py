from django.shortcuts import render
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required

# username: test_user / test_user2
# password: sifre123


@login_required
def ReceiptListView(request):
    context = {"receipts": Receipt.objects.filter(purchaser=request.user)}

    return render(request, "receipts/home.html", context)
