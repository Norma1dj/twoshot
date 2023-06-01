from django.contrib import admin
from receipts.models import Receipt, Account, ExpenseCategory

# Register your models here.
@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ()

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ()
    
@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ()
