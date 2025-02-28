def compare():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    if first_number > second_number:
        print(f"{first_number} is greater than {second_number}")
    elif first_number < second_number:
        print(f"{second_number} is greater than {first_number}")
    else:
        print(f"{first_number} and {second_number} is equal")
compare()