#create for loop with 101 iterations
for numbers in range(101):
#use remainder of dividing by 10 and 5 to exclude numbers ending in 5 and 0
    if numbers % 10 != 0 and numbers % 5 != 0:
#print result
        print(numbers)