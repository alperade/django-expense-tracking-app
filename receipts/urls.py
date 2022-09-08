from django.urls import path

from receipts.views import (
    ReceiptListView,
    ReceiptCreateView,
    ExpenseCategoryListView,
    AccountListView,
    ExpenseCategoryCreateView,
)

urlpatterns = [
    path("", ReceiptListView, name="home"),
    path("create/", ReceiptCreateView, name="create_receipt"),
    path("categories/", ExpenseCategoryListView, name="list_categories"),
    path("accounts/", AccountListView, name="accounts"),
    path(
        "categories/create/", ExpenseCategoryCreateView, name="create_category"
    ),
]
