import random

money = 100

# Write your game of chance functions here
def handle_winloss(amount_cash, won_bool):
	if won_bool:
		return amount_cash
	else:
		return amount_cash * -1

def update_wallet(amount_cash):
	global money
	money += amount_cash
	print("--------")
	if money < 0:
		print("You owe the House ${}.".format(money * -1))
	else:
		print("You have ${} in your wallet.".format(money))

def coin_flip(player_bet, player_choice):
	cash_difference = 0
	player_won = False
	
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
	
	cash_difference = handle_winloss(player_bet, player_won)
	if cash_difference < 0:
		print("You lost ${} by guessing {}...".format(player_bet, player_choice))
	else:
		print("You got ${} by guessing {}!".format(player_bet, player_choice))
	
	return cash_difference

def cho_han(player_bet, player_choice):
	cash_difference = 0
	player_won = False
	
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
	
	cash_difference = handle_winloss(player_bet, player_won)
	if cash_difference < 0:
		print("You lost ${} by guessing {}...".format(player_bet, player_choice))
	else:
		print("You got ${} by guessing {}!".format(player_bet, player_choice))
	
	return cash_difference

def card_versus(player_bet):
	cash_difference = 0
	player_won = False
	
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
		print("You whooped Player 2 with your superior card-drawing skills! His left eye has developed a twitch.")
		player_won = True
	elif player_1_card < player_2_card:
		print("\"You lost, fair and square...\" your opponent grins. You feel yourself getting red in the face.")
	else:
		print("Your opponent shrugs. \"Rematch?\"")
		return cash_difference				# Player doesn't win or lose cash.
	
	cash_difference = handle_winloss(player_bet, player_won)
	if cash_difference < 0:
		print("You got swindled for ${}! How foolish of you.".format(player_bet))
	elif cash_difference == 0:
		print("No money was exchanged.")
	else:
		print("You earned ${} from your opponent! It feels good to be the king.".format(player_bet))
	
	return cash_difference

# Call your game of chance functions here

# For-loop calls coin_flip() X times.
X = 6
for i in range(X):
	if bool(random.randint(0, 1)):
		guess = "Heads"
	else:
		guess = "Tails"
	update_wallet(coin_flip(100, guess))

# For-loop calls cho_han() Y times.
Y = 6
for i in range(Y):
	if bool(random.randint(0, 1)):
		guess = "Even"
	else:
		guess = "Odd"
	update_wallet(cho_han(100, guess))

# For-loop calls card_versus() Z times.
Z = 6
for i in range(Z):
	update_wallet(card_versus(100))
