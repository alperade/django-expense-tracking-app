from django.urls import path

from receipts.views import ReceiptListView, ReceiptCreateView

urlpatterns = [
    path("", ReceiptListView, name="home"),
    path("create/", ReceiptCreateView, name="create_receipt"),
]
