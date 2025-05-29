from external_api import convert_to_rub

def get_transaction_amount_rub(transaction: dict) -> float:
    """
    Возвращает сумму транзакции в рублях (float), конвертируя при необходимости.
    """
    amount = transaction.get("amount")
    currency = transaction.get("currency", "RUB")
    return convert_to_rub(amount, currency)