from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Expense, Balance
from .serializers import ExpenseSerializer, BalanceSerializer
from django.http import HttpResponse
import os
from django.conf import settings
# Create your views here.
from .utils import calculate_splits,generate_excel_sheet

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        expense = serializer.save(creator=self.request.user)
        calculate_splits(expense)
    
    @action(detail=False, methods=['get'],permission_classes=[permissions.IsAuthenticated])
    def download_balance_sheet(self, request):
        user_balances = Balance.objects.all()
        excel_file = generate_excel_sheet(user_balances)
        folder_path = os.path.join(settings.MEDIA_ROOT, 'balance_sheets')  # Save in 'media/balance_sheets/' folder
        os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist
        
        file_path = os.path.join(folder_path, 'balance_sheet.xlsx')
        with open(file_path, 'wb') as f:
            f.write(excel_file)  
        response = HttpResponse(excel_file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=balance_sheet.xlsx'
        return response
        
class BalanceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.action == 'list':
            return Balance.objects.all()
        
    
        return super().get_queryset()  
    

