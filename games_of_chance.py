import random

money = 100

# Write your game of chance functions here
def coin_flip(player_bet, player_choice):
	cash_difference = 0
	player_won = False						# The player hasn't won yet.
	
	coin_is_heads = bool(random.randint(0, 1))
	print("\ncoin_is_heads = {}".format(coin_is_heads))
	
	if player_choice == "Heads" and coin_is_heads:
		print("Heads! You got it!")
		player_won = True
	elif player_choice == "Tails" and (not coin_is_heads):
		print("Tails! Nice one!")
		player_won = True
	else:
		print("Better luck next time.")
	
	if player_won:
		cash_difference = player_bet
	else:
		cash_difference = player_bet * -1
	
	return cash_difference

def cho_han(player_bet, player_choice):
	cash_difference = 0
	player_won = False						# The player hasn't won yet.
	
	die1 = random.randint(1, 6)
	die2 = random.randint(1, 6)
	sum_of_dice = die1 + die2
	print("\n{} + {} = {}".format(die1, die2, sum_of_dice))
	
	sum_is_even = sum_of_dice % 2 == 0
	
	if player_choice == "Even" and sum_is_even:
		print("Even. Good work!")
		player_won = True
	elif player_choice == "Odd" and (not sum_is_even):
		print("Odd! Nice.")
		player_won = True
	else:
		print("Sorry, chump - the House wins.")
	
	if player_won:
		cash_difference = player_bet
	else:
		cash_difference = player_bet * -1
	
	return cash_difference

def card_versus(player_bet):
	cash_difference = 0
	player_won = False						# The player hasn't won yet.
	
	card_deck = []
	for i in range(4):						# Four suits...
		for j in range(1, 14):				# 13 cards per suit...
			card_deck.append(j)
	random.shuffle(card_deck)				# Shuffle the new deck.
	
	# Each player draws a card.
	player_1_card = card_deck.pop(random.choice(range(len(card_deck))))
	player_2_card = card_deck.pop(random.choice(range(len(card_deck))))
	print("\nYou drew {}.\nYour opponent drew {}.".format(player_1_card, player_2_card))
	
	if player_1_card > player_2_card:
		print("You beat Player 2!")
		player_won = True
	elif player_1_card < player_2_card:
		print("You lost to Player 2.")
	else:
		print("You tied with Player 2!")
		return cash_difference				# Player doesn't win or lose cash.
	
	if player_won:
		cash_difference = player_bet
	else:
		cash_difference = player_bet * -1
	
	return cash_difference
	

# Call your game of chance functions here

# For-loop calls coin_flip() X times.
#X = 6
#for i in range(X):
#	if bool(random.randint(0, 1)):
#		guess = "Heads"
#	else:
#		guess = "Tails"
#	print("You got ${} by guessing {}!".format(coin_flip(100, guess), guess))

# For-loop calls cho_han() Y times.
#Y = 6
#for i in range(Y):
#	if bool(random.randint(0, 1)):
#		guess = "Even"
#	else:
#		guess = "Odd"
#	print("You got ${} by guessing {}!".format(cho_han(100, guess), guess))

# For-loop calls card_versus() Z times.
Z = 6
for i in range(Z):
	print("You got ${} from your opponent!".format(card_versus(100)))
