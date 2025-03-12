#create for loop, 101 iterations, get remainder from divided by 10 to exclude numbers ending in 0
for numbers in range(101):
    if numbers % 10 != 0:
        print(numbers)