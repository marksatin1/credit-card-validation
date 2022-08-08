README

Given a credit card number, credit.py validates its authenticity by verifying its checksum. Every authentic credit card number must pass a series of mathematical checks that are built into the number itself. Some of these checks are specific to the credit card company and others are agnostic. credit.py can verify Amex, Mastercard, and Visa cards.

credit.py takes no arguments. It prompts the user to enter a credit card number and will exit if the input is not an integer or a valid credit card number length.

Once past these initial checks, the module looks at the odd digits starting from the last digit and multiplies them by 2. If any of these products are double digits their individual digits get added together. For example, 11 => 1 + 1 = 2. Each of these digits is added to the sum. The even digits are then added to the sum.

If the sum is an odd number then the credit card is INVALID and the program exits. Otherwise it checks the number of digits in the card and the value of specific digits to determine which company has issued the card.

EXPECTED OUTPUTS

AMEX
MASTERCARD
VISA
INVALID
