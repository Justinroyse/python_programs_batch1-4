def even_checker(num):
    counter = 0
    for item in num[0:]:
        if item % 2 == 0:
            counter += 1
    return counter




program = [int(input( f"Enter number ({i+1}):  ")) for i in range(10)]
print(even_checker(program))
