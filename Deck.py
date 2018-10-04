'''
The Deck Class
'''
from Card import Card
import random

class Deck():
	"""docstring for Deck"""

	# the initialisation
	def __init__(self):
		self.cards = []
		self.card_setup()

	def reset_deck(self):
		self.cards = []
		self.card_setup()
	# if you ever want to print the Deck	
	# def __str__(self):
	# 	string = ''
	# 	for card in self.cards:
	# 		string += str(card) + '\n'
	# 	return string 

	# filling up the deck
	def card_setup(self):
		houses = {'CLUBS', 'SPADES', 'HEARTS', 'DIAMONDS'}
		face_values = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
		for house in houses:
			for value in face_values:
				self.cards.append(Card(value, house))

	def shuffle(self):
		random.shuffle(self.cards)