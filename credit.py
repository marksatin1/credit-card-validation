## Validate a credit card number ##
import sys

card = input("Credit Card Number: ")
try:
  card = int(card)
except ValueError:
  sys.exit("Input is not an integer")

card = str(card)
digits = len(card)
if digits != 13 and digits != 15 and digits != 16:
  sys.exit("Invalid Credit Card length.")

list = []
for i in range(digits):
  list.append(card[i])

sum = 0
digit = 0
list.reverse()
for index, digit in enumerate(list):
  if index % 2 != 0:
    digit = int(digit) * 2
    if digit > 9:
      d = (digit // 10) + (digit % 10)
      sum += d
    else:
      sum += digit
  else:
    digit = int(digit)
    sum += digit

list.reverse()
if sum % 10 == 0:
  if digits == 15 and list[0] == '3':
    if list[1] == '4' or '7':
      print("AMEX")
  if digits == 16 and list[0] == '5':
    if list[1] == '1' or '2' or '3' or '4' or '5':
      print("MASTERCARD")
  if digits == 13 or 16 and list[0] == '4':
    print("VISA")
else:
  print("INVALID")