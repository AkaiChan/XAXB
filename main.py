import random

intStart = input("Please input start of period:")
intEnd = input("Please input end of period:")

intAnswer = random.randint(int(intStart),int(intEnd))
count = 0
while True:
	count += 1
	intInput = input("Please inuput number: ")
	intInput = int(intInput)
	if intInput == intAnswer:
		print("Correct")
		print("Total ", count , " times")
		break
	else:
		print("Incorrect!")
		if intInput > intAnswer:
			print("Guess smaller")
		else:
			print("Guess bigger")
	print("it's the " , count , " times")
