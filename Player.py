'''
The Player Class
'''
from Card import Card

class Player():
	"""docstring for Player"""
	def __init__(self, name, chips=100):
		self.name = name
		self.chips = chips
		self.cards = []

	# prints the player's status
	def __str__(self):
		return 'Name: ' + self.name + '\nChips: ' + str(self.chips)

	# deducts the players chips
	def deduct(self, deduction):
		self.chips -= deduction	

	# increases players chips
	def increase(self, gain):
		self.chips += gain

	# calculates the value of cards
	def value_calculator(self):
		total = 0
		# calculate the total values
		for card in self.cards:
			total += card.card_value()
		# subtract 10 for every extra Ace card
		for card in self.cards:
			if(card.card_value() == 11 and total>21):
				total -= 10
		return total