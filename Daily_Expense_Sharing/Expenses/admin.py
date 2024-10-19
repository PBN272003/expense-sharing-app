
from django.contrib import admin
from .models import Expense, ExpenseParticipant, Balance

# Register your models here.

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'creator', 'date', 'split_type')
    search_fields = ('description', 'creator__username', 'amount')
    list_filter = ('split_type', 'date')
    ordering = ('-date',)  # Orders by most recent expenses

@admin.register(ExpenseParticipant)
class ExpenseParticipantAdmin(admin.ModelAdmin):
    list_display = ('expense', 'user', 'amount_owed', 'percentage')
    search_fields = ('user__username', 'expense__description')
    list_filter = ('expense',)

@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')
    search_fields = ('user__username',)
    list_filter = ('amount',)


# Register your models here.
