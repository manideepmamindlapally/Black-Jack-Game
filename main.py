'''
The main program
'''
from Deck import Deck
from Player import Player
from Dealer import Dealer

import mainfunc

player_name = input("What is your name: ")
player = Player(player_name)
print('=============================================')
print("              BLACK-JACK-GAME                ")
print('=============================================')
print("Type 'QUIT' anytime to quit the game")

# each game loop
while True:
	game_deck = Deck()
	game_dealer = Dealer()
	bet = mainfunc.initialise_game(player, game_deck, game_dealer)
	# each round loop
	while True:
		mainfunc.print_cards(player, game_dealer)

		# check conditions
		if(mainfunc.round_checker(player, game_dealer) > 0):
			mainfunc.game_over(mainfunc.round_checker(player, game_dealer), bet, player)
			break

		game_deck.shuffle()

		player_choice = input("What would you like to do? Press (1) for STAY (2) for HIT: ")
		mainfunc.round_choice(player_choice, player, game_dealer, game_deck)
	
	# exit the game when balance below zero
	if(player.chips <= 0):
		break
print("=================================================")
print("                G A M E   O V E R")
print("Thank you for playing! But you have lost the game")
print("=================================================")
