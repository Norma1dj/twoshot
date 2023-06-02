from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import CreateReceiptForm
# Create your views here.

@login_required()
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        'receipts': receipts
    }
    return render(request, "receipt_list.html", context)


@login_required
def create_receipt(request):

    if request.method == "POST":

        form = CreateReceiptForm(request.POST)
        if form.is_valid(): 
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()

            return redirect("home")

    else:
        form = CreateReceiptForm()

    context = {
        "form": form,
    }
    return render(request, "create_receipt.html", context)


@login_required()
def category_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        'categories': categories
    }
    return render(request, "category_list.html", context)


def account_list(request):
    accounts = Account.objects.filter(owner=request.user)
    context = {
        'accounts': accounts
    }
    return render(request, "account_list.html", context)