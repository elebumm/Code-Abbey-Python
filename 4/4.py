#Calculates lowest numbers out of numbers inputted.

print('How many sets of numbers would you like to go through?')
answer_numbers = raw_input('> ')

storage = []

for x in range(0, int(answer_numbers)):
    print('What is your first number for set #%d' % x)
    first_answer = raw_input('> ')
    print('What is your second numher for set #%d' % x)
    second_answer = raw_input('> ')
    if (int(first_answer) > int(second_answer)):
        storage.append(int(second_answer))
    elif (int(first_answer) == int(second_answer)):
        storage.append('These 2 numbers are equal')
    else:
        storage.append(int(first_answer))

print(storage)