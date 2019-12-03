import random

intAnswer = random.randint(1,100)
while True:
	intInput = input("Please inuput number: ")
	intInput = int(intInput)
	if intInput == intAnswer:
		print("Correct")
		break
	else:
		print("Incorrect!")
		print(intAnswer)
		if intInput > intAnswer:
			print("Guess smaller")
		else:
			print("Guess bigger")
