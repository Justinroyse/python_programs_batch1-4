numbers = []
print("*****Sum Calculator*****")
print("\n")

for i in range(10):
    store = (input(f"Enter number {i + 1}: "))
    numbers.append(int(store))

print(sum(numbers))