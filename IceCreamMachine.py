### Program that creates an Ice-Cream Cone

#Inventory in Dictionaries
cone_stock = {'plain' : 1, 'chocolate' : 1.50, 'sprinkled' : 1.20}
flavour_stock = {'strawberry': 2.00 , 'banana' : 2.25 , 'mango': 2.75 , 'cherry': 2.15}
topping_stock = {'oreos': 1.00 , 'walnuts' : 0.50 , 'sprinkles': 0.75, 'none' : 0}

#Variables
subtotal = 0
cones_list = list(cone_stock.keys())
flavour_list = list(flavour_stock.keys())
topping_list = list(topping_stock.keys())
flavour_stock_copy = dict.copy(flavour_stock)


while True:

	### Intro Speech from Robot
	print("\nWelcome to the Virtual Ice Cream Shop. May I take your order?")
	step_1 = input("Type 'Yes' to proceed. \nType 'Goodbye' to exit program.\n")
	options_1 = ['Yes', 'Goodbye']


### Accounting for user input not willing to follow through with program
	if step_1.title() not in options_1:
		print("\nI don't understand. Please try again.")
	elif step_1.title() == "Goodbye":
		print("Thank You for visiting us. We hope to see you again.")
		break

### Cone Options
	elif step_1.title() == "Yes":
		print("\nToday we have the following cone options: ")

		for cones, cone_prices in cone_stock.items():
			print("- " + cones.title() + " : $" +  str(cone_prices))

		step_2 = input("\nWhat cone would you like?\n")

		if step_2.lower() not in cones_list:
			print("\nUh Oh. We don't have that option. Start Over.")
			continue
		else:
			print ("\nExcellent choice. Lets proceed.")

### Flavour Options

		print("\nOur flavours are the following: ")
		for flavour, flavour_prices in flavour_stock.items():
			print("- " + flavour.title() + " : $" +  str(flavour_prices))
		step_3 = input("\nSo what'll it be?\n")

		if step_3.lower() not in flavour_list:
			print("\nUh Oh. We don't have that option. Start Over.")
			continue

			
### 2nd Flavour Option
		else:
			print ("\nMy man! Can I offer you another flavour? On me.")
			answer = input('Yes or No?\n')
			if answer.lower() == 'yes':
				print("\nPick one: ")
				for flavour_add in flavour_stock.keys():
					print("- " + flavour_add.title())
				step_3add = input("")
				if step_3add.lower() not in flavour_list:
					print("\nUh Oh. We don't have that option. Start Over.")
					continue
				else:
					print("Awesome. Let's continue.")
			elif answer.lower() == 'no':
				print("\nGotcha.")
				step_3add = ''
			else:
				print("Sorry, I don't understand. Let's start over.")
				continue


### Toppings Options
		print("\nAny toppings? Here's what we have: ")
		for toppings, toppings_prices in topping_stock.items():
			print("- " + toppings.title() + " : $" +  str(toppings_prices))
		step_4 = input("")

		if step_4.lower() not in topping_list:
			print("\nUh Oh. We don't have that option. Start Over.")
			continue
		else:
			print ("\nDone. Let me ring you up!")

		if step_4.lower() == 'none':
			step_4 = 'no'
		if step_4.lower() == 'walnuts':
			step_4 = 'walnut'
		if step_4.lower() == 'sprinkles':
			step_4 = 'sprinkle'
		if step_4.lower() == 'oreos':
			step_4 = 'oreo'

### Order Total Calculation
		if step_2.lower() == 'plain':
			subtotal += subtotal + 1
		elif step_2.lower() == 'chocolate':
			subtotal += subtotal + 1.5
		elif step_2.lower() == 'sprinkled':
			subtotal += subtotal + 1.2

		if step_3.lower() == 'strawberry':
			subtotal += subtotal + 2
		elif step_3.lower() == 'banana':
			subtotal += subtotal + 2.25
		elif step_3.lower() == 'mango':
			subtotal += subtotal + 2.75
		elif step_3.lower() == 'cherry':
			subtotal += subtotal + 2.15

		if step_3.lower() == 'oreos':
			subtotal += subtotal + 1
		elif step_3.lower() == 'sprinkles':
			subtotal += subtotal + 0.75
		elif step_3.lower() == 'walnuts':
			subtotal += subtotal + 0.50
		elif step_3.lower() == 'none':
			subtotal += subtotal + 0

#End of Transaction
		total_cost = subtotal
		if step_3add == '':
			order_message = ("You've ordered " + step_3.lower() + " ice cream" + " with " + step_4.lower() + " toppings, on the " + step_2.lower() + " cone.")
			print(order_message)
		elif step_3add.lower() == step_3.lower():
			print("You've ordered " + "double " + step_3.lower() + " ice cream" + " with " + step_4.lower() + " toppings, on the " + step_2.lower() + " cone.")
		else:
			print("You've ordered " + step_3.lower() + " and " + step_3add.lower() + " ice cream" + " with " + step_4.lower() + " toppings, on the " + step_2.lower() + " cone.")

		print("$" + str(subtotal) + ", Please.")
		break


