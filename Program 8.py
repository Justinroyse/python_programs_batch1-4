store = []
counter = 0
for i in range(10):
    given = int(input(f"Enter number ({i+1}): "))
    store.append(given)
    if given % 2 != 0:
        counter += 1
    else:
        pass
print(counter)
