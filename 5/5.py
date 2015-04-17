#This program requires you to input the amount of times you want to iterate through a loop and puts in 3 numbers
#and finds the lowest one.


#This one is oddly complicated. I just gave up on it.






print('Welcome to Exercise #5. Please enter the amount of times you would like to loop.')
number_of_loops = raw_input('> ')


storage = []

#I add 1 to the number_of_loops variable just so that when we output the loop number it starts at 1 rather than 0
number_of_loops_for_loop = int(number_of_loops) + 1

for x in range(1, number_of_loops_for_loop):
    print('Please enter your first number for loop #%d' % x)
    first_number = raw_input('> ')
    print('Please enter your second number for loop #%d' % x)
    second_number = raw_input('> ')
    print('Please enter your third number for loop #%d' % x)
    third_number = raw_input('> ')
    if(int(first_number) > int(second_number)):
        if(int(second_number) > int(third_number)):
            storage.append((third_number))
        elif int(second_number) < int(third_number):
            storage.append(second_number)
        else:
            storage.append(first_number)
    if(int(first_number) < int(second_number)):
        if(int(first_number) < int(third_number)):
            storage.append(first_number)
        elif(int(first_number) > int(third_number)):
            storage.append(third_number)
    else:
        storage.append(first_number)

print(storage)