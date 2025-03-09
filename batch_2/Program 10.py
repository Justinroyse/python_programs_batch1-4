num1 = int(input("Enter a number (1):  "))
num2 = int(input("Enter a number (2):  "))

if num1 > num2:
    numbers = list(range(num2, num1+1))
elif num2 > num1:
    numbers = list(range(num1, num2+1))
else:
    pass

print(numbers)