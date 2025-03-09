import math

program = [int(input(f"Enter number ({i+1}):  ")) for i in range(2)]
print(math.trunc(program[0]/program[1]))