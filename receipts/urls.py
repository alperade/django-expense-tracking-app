from django.urls import path

from receipts.views import (
    ReceiptListView,
    ReceiptCreateView,
    ExpenseCategoryListView,
    AccountListView,
)

urlpatterns = [
    path("", ReceiptListView, name="home"),
    path("create/", ReceiptCreateView, name="create_receipt"),
    path("categories/", ExpenseCategoryListView, name="categories"),
    path("accounts/", AccountListView, name="accounts"),
]
