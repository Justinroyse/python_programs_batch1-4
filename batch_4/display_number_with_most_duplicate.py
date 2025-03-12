#create function to check for duplicates, display duplicate with most number
def duplicate_checker(given):
    duplicates = []
    seen = set()

    for numbers in given:
        if numbers in seen and numbers not in duplicates:
            duplicates.append(numbers)
        else:
            seen.add(numbers)
	
    for numbers in duplicates:
        highest_checker = duplicates[0]
        highest_counter = 0
        
#create while loop user input until invalid
#print result