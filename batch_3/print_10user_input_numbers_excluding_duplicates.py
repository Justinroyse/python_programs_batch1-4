#function that checks for duplicates and displays numbers that don't have duplicates
def duplicate_checker(given):
    stored_items = given[0]
    for items in given[1:]:
        if stored_items != items:
            print(items)

#for loop inside a list used for user number inputs
