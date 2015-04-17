#This asks the user to input 2 numbers then adds them. 
#I imported time for the extra suspense :)


import time

print('Welcome to Exercise #1!')
time.sleep(3)
print('Today we are going to add 2 numbers!')
time.sleep(2)
print('Please enter your first number!')
first_number = int(raw_input('> '))
print('Please enter your second number!')
second_number = int(raw_input('> '))

result = int(first_number) + int(second_number)

print("You're number is... " + str(result))