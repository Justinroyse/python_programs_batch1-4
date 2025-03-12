#initialize counter
counter = -1

#while loop to print 0-100 numbers
while counter != 100:
    counter += 1
    #print only odd number by dividing by 2 not equal to 0
    if counter % 2 != 0:
        print(counter)