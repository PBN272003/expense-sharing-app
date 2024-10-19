from rest_framework import serializers
from .models import Expense, ExpenseParticipant, Balance
from Users.serializers import CustomUserSerializer
from datetime import datetime
from Users.models import CustomUser



class ExpenseSerializer(serializers.ModelSerializer):
    participants = serializers.ListField(write_only=True) 
    
    class Meta:
            model = Expense
            fields = ['id','amount','date','description','split_type', 'creator', 'participants']
            extra_kwargs = {
             'date': {'required': False},          # Make 'date' optional
             'description': {'required': False}    # Make 'description' optional
            }
        
    def create(self, validated_data):
            participants_data = validated_data.pop('participants')
            if 'date' not in validated_data:
                 validated_data['date'] = datetime.now().date()

            if 'description' not in validated_data:
                 validated_data['description'] = "No description provided"
            expense = Expense.objects.create(**validated_data)
            
            for participant in participants_data:
                user_id = participant['user']
                user = CustomUser.objects.get(id=user_id) 
                amount_owed = participant['amount_owed']
                ExpenseParticipant.objects.create(expense=expense, user=user, amount_owed=amount_owed)
            
            return expense

class ExpenseParticipantSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ExpenseParticipant
        fields = ['id', 'user', 'user_id', 'amount_owed', 'percentage']

class BalanceSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Balance
        fields = ['id', 'user', 'amount']
    