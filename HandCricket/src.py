import random as r

run = 0
while True:
	try:
		user_input = int(input("Enter a number: "))
	except:
		print("Invalid input...")
		continue

	computer_number = r.randint(1, 6)
	print(computer_number)

	if computer_number == user_input:
		print("OUT")
		break
	elif user_input == -1:
		print("Your total score is: ", run)
	elif user_input == -1:
		print("Your total score is: ", run)
	else:
		run += user_input
