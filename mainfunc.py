'''
The main Functions
'''
from Card import Card
from Deck import Deck
from Player import Player

def initialise_game(player, game_deck, game_dealer):
	reset_game(player, game_deck, game_dealer)

	print(f"Your available chips: {player.chips}")
	bet = int(input("What is your bet in chips: "))
	if bet > player.chips:
		print("Sorry! You can't bet more than what you have")
		return initialise_game(player, game_deck, game_dealer)
	return bet

def reset_game(player, game_deck, game_dealer):
	# initialise
	player.cards = []
	game_dealer.cards = []
	game_deck.reset_deck()
	game_deck.shuffle()
	# assign the first two cards to the player, the next two cards to the dealer -- this is random
	player.cards = game_deck.cards[:2]
	game_dealer.reserved_card = game_deck.cards[2]
	game_dealer.cards = game_deck.cards[3:4]
	# now, remove the assigned cards from the decks
	game_deck.cards = game_deck.cards[4:]

# checks the value of cards after each round
def round_checker(player, dealer):
	if(player.value_calculator() == 21):
		return 1
	if(dealer.value_calculator() > 21 and player.value_calculator() < 21):
		return 1
	if(player.value_calculator() > 21):
		return 2
	if(dealer.value_calculator() > player.value_calculator()):
		return 2
	return 0

# prompt screen after the round gets over
def game_over(num, bet, player):
	print("-----------------------------------")
	print("           round over")
	if(num == 1):
		print(f"You have won {bet} chips")
		player.increase(bet)
	elif(num == 2):
		print(f"You have lost {bet} chips") 
		player.deduct(bet)
	print("-----------------------------------")

# print cards after every round
def print_cards(player, game_dealer):
	print("================================================")
	print("                  DEALER ")
	print("------------------------------------------------")
	for card in game_dealer.cards:
		print(card)
	print(Card('RESERVED', 'CARD'))
	print("================================================")
	print(f"                  {player} ")
	print("------------------------------------------------")
	for card in player.cards:
		print(card)

# The STAY-1 and HIT-2 options
def round_choice(choice, player, game_dealer, game_deck):
	if(int(choice) == 2):
		player.cards.append(game_deck.cards[0])
		game_deck.cards = game_deck.cards[1:]
	game_dealer.cards.append(game_deck.cards[0])
	game_deck.cards = game_deck.cards[1:]
