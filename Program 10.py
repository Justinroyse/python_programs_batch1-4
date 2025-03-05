num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 < num2:
    numbers = list(range(num1, num2 + 1))
elif num1 > num2:
    numbers = list(range(num2, num1 + 1))
else:
    numbers = [num1]

print(numbers)
