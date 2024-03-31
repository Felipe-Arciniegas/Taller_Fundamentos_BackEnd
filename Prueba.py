def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Invalid currency"
    
    conversion_rate = exchange_rates[from_currency] / exchange_rates[to_currency]
    converted_amount = amount * conversion_rate
    
    return converted_amount