from django.contrib import admin

from receipts.models import (
    ExpenseCategory,
    Account,
    Receipt,
)


class ExpenseCategoryAdmin(admin.ModelAdmin):
    pass


class AccountCategoryAdmin(admin.ModelAdmin):
    pass


class ReceiptCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
admin.site.register(Account, AccountCategoryAdmin)
admin.site.register(Receipt, ReceiptCategoryAdmin)
