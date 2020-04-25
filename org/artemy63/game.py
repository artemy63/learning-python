import random

number = random.randint(0,101)

while True:

	answer = input("Input a digit: ")
	
	if not answer or answer == "exit":
		break
		
	if not answer.isdigit():
		print("Please input a number!")
		continue
		
	user_answer = int(answer)
	
	if user_answer < number:
		print("more please")
	elif user_answer > number:
		print("less please")
	else:
		print("Right!")
		break