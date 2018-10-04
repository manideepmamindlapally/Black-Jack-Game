'''
The Dealer class
'''
from Card import Card

class Dealer():
	"""docstring for Delaer"""
	def __init__(self):
		self.cards = []
		self.reserved_card = Card()

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