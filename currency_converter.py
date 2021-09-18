from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = int(input('Inserisci la quantità che devi convertire : '))

from_currency = input('Da (es. USD): ').upper()
to_currency = input('A (es. EUR): ').upper()

print(from_currency, 'a', to_currency)
result = c.convert(from_currency, to_currency, amount)
print(result)