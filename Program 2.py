program = [int(input(f"Enter number ({i+1}): ")) for i in range(2)]
if program[0] == program[1]:
    print("Equal")
else:
    print("Not Equal")