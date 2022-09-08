from django.urls import path

from receipts.views import ReceiptListView

urlpatterns = [
    path("", ReceiptListView, name="home"),
]
