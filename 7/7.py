#Challenge 7: Fahrenheit to Celsius
#Equation: (F - 32) * 5/9 + 32 = C
print("Hello! Thank you for choosing Fahrenheit to Celcius calulator.")
print("please enter the amount of numbers you want to convert.")

userInput = input("> ")
choices = int(userInput)

numbers = []

for x in range(1, choices + 1):
	print("Please enter choice #" + str(x) + ".")
	fNumber = int(input("> "))
	print("You just entered the number " + str(fNumber))
	cNumber = (fNumber - 32) * 5/9 
	numbers.append(cNumber)


print(numbers)
