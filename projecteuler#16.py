# Power Digit Sum

number = 2 ** 1000
digits = [int(digit) for digit in str(number)]
#print(digits)
total = sum(digits)
print("The total is " + str(total))