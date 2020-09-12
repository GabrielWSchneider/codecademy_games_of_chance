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

# Call your game of chance functions here

# The following for loop calls coin_flip X times.
X = 6
for i in range(X):
	if bool(random.randint(0, 1)):
		guess = "Heads"
	else:
		guess = "Tails"
	print("You got ${} by guessing {}!".format(coin_flip(100, guess), guess))
