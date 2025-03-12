#create 2 variable for user inputs
num1 = int(input("Enter a number (1):  "))
num2 = int(input("Enter a number (2):  "))
#create if else logic and implement list function to determine range between 2 user input numbers
if num1 > num2:
    numbers = list(range(num2, num1+1))
elif num2 > num1:
    numbers = list(range(num1, num2+1))
else:
    pass
#print the result numbers between 2 user input
print(numbers)