def even_check(num):
    counter = 0
    for i in num[0:]:
        if i % 2 == 0:
            counter += 1
    return counter

program = [int(input(f"Enter number ({i+1}):  ")) for i in range(10)]
print(even_check(program))