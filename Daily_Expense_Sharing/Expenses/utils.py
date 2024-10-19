from decimal import Decimal
from .models import Balance
from openpyxl import Workbook
from io import BytesIO

def calculate_splits(expense):
    total_amount = expense.amount
    participants = expense.participants.all()
    num_participants = participants.count()

    if expense.split_type == 'EQUAL':
        amount_per_person = total_amount / num_participants
        for participant in participants:
            participant.amount_owed = amount_per_person
            participant.save()
            update_balance(participant.user, -amount_per_person)
    elif expense.split_type == 'EXACT':
        for participant in participants:
            update_balance(participant.user, -participant.amount_owed)
    elif expense.split_type == 'PERCENTAGE':
        for participant in participants:
            amount_owed = (participant.percentage / 100) * total_amount
            participant.amount_owed = amount_owed
            participant.save()
            update_balance(participant.user, -amount_owed)

    update_balance(expense.creator, total_amount)

def update_balance(user, amount):
    balance, created = Balance.objects.get_or_create(user=user)
    balance.amount += Decimal(amount)
    balance.save()
    
def generate_excel_sheet(balances):
    wb = Workbook()
    ws = wb.active
    ws.title = "Balance Sheet"

    headers = ["User", "Balance"]
    ws.append(headers)

    for balance in balances:
        ws.append([balance.user.username, float(balance.amount)])

    excel_file = BytesIO()
    wb.save(excel_file)
    excel_file.seek(0)

    return excel_file.getvalue()