import decimal
from decimal import ROUND_DOWN, ROUND_UP, Decimal, getcontext

decimal_a = decimal.Decimal('0.2')
decimal_b = decimal.Decimal('0.1')
print(decimal_a + decimal_b)  # 0.3 

getcontext().prec = 6
print(Decimal("1") / Decimal("7"))

getcontext().prec = 8
print(Decimal("1") / Decimal("7"))
print(Decimal("3.1415926535897932384626433832795") +0) # 3.141593

number = Decimal('3.14159')
# Встановлення точності до двох знаків після коми
rounded_number = number.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
print(rounded_number)