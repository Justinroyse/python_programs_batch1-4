num1 = int(input("Enter a number (1):   "))
num2 = int(input("Enter a number (2):   "))

if num1 < num2:
    store = list(range(num1, num2+1))
elif num1 > num2:
    store = list(range(num2, num1+1))
else:
    pass

print(store)