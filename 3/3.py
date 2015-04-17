print('Please enter the amount of equations you would like solved')
amount_of_numbers = raw_input('> ')

amount_of_numbers_for_loop = int(amount_of_numbers) + 1

storage = []

for x in range(1, int(amount_of_numbers_for_loop)):
    print('Enter first number in %d equation' % x)
    first_number = raw_input('> ')
    print('Enter second number in %d equation' % x)
    second_number = raw_input('> ')
    result = int(first_number) + int(second_number)
    storage.append(result)

print(storage)
