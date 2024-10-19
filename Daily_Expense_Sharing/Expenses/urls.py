from django.urls import path
from .views import ExpenseViewSet, BalanceViewSet

urlpatterns = [
    # Expense URLs
    path('', ExpenseViewSet.as_view({'get': 'list', 'post': 'create'}), name='expense-list'),
    path('<int:pk>/', ExpenseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='expense-detail'),
    
    # Balance URLs
    path('balances/', BalanceViewSet.as_view({'get': 'list'}), name='balance-list'),
    path('balances/<int:pk>/', BalanceViewSet.as_view({'get': 'retrieve'}), name='balance-detail'),
    path('download-balance-sheet/', ExpenseViewSet.as_view({'get': 'download_balance_sheet'}), name='download-balance-sheet'),
]