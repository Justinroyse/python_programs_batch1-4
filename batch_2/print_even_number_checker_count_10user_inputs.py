#create even_check function and count the even numbers
def even_check(numbers):
    counter = 0
    for number in numbers[0:]:
        if number % 2 == 0:
            counter += 1
    return counter

#create list for 10 user input
program = [int(input(f"Enter number ({numbers+1}):  "))
           for numbers in range(10)]

#print result using even_check function
print(even_check(program))