print('How many numbers do you want to add?')
amount_of_numbers = raw_input('> ')

result = 0

for x in range(0, int(amount_of_numbers)):
    print('Please enter the number you want to add.')
    add_number = int(raw_input('> '))
    result += add_number

print(result)