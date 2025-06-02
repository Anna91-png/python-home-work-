from src.utils import get_transactions

transactions = get_transactions("data/operations.json")
print(transactions)
print(f"Прочитано транзакций: {len(transactions)}")
print("Первые 2 транзакции:")
for tx in transactions[:2]:
    print(tx)
