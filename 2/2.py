#You enter how many numbers you want to be added and the number you enter will
#go through a loop to and add it to a variable. Simple but kinda fun.

print('How many numbers do you want to add?')
amount_of_numbers = raw_input('> ')

result = 0

for x in range(0, int(amount_of_numbers)):
    print('Please enter the number you want to add.')
    add_number = int(raw_input('> '))
    result += add_number

print(result)