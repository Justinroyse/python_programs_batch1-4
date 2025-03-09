def difference(given):
    operation = given[0]
    for items in given[1:]:
        operation -= items
    return operation

program = [int(input(f"Enter number ({i+1}):  ")) for i in range(10)]
print(difference(program))
