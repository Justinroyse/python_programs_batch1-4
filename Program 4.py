import math
store = []
for i in range(2):
    given = int(input(f"Enter number ({i+1}):  "))
    store.append(given)
print(math.trunc(store[0] / store[1]))
