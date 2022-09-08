from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm


# username: test_user / test_user2
# password: sifre123


@login_required
def ReceiptListView(request):
    context = {"receipts": Receipt.objects.filter(purchaser=request.user)}

    return render(request, "receipts/home.html", context)


@login_required
def ReceiptCreateView(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.purchaser = request.user
            plan.save()
            form.save_m2m()
            return redirect("home")
    else:
        form = ReceiptForm()
    context = {"form": form}
    return render(
        request,
        "receipts/create.html",
        context,
    )


@login_required
def ExpenseCategoryListView(request):
    context = {
        "categories": ExpenseCategory.objects.filter(owner=request.user)
    }

    return render(request, "categories/list.html", context)


@login_required
def AccountListView(request):
    context = {"accounts": Account.objects.filter(owner=request.user)}

    return render(request, "accounts/list.html", context)
