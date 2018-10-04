'''
The Card Class
'''
class Card():
	"""docstring for Card"""
	# intitialisation
	def __init__(self, face_value='NIL', house='NIL'):
		self.face_value = face_value
		self.house = house
		
	# return a string to print the card
	def __str__(self):
		return '==================\n||       {}       ||\n||    {}     ||'.format(self.face_value, self.house)

	# returns the card value
	def card_value(self):
		# error handling: if face_value is an integer, return it
		try:
			return int(self.face_value)
		except:
			if self.face_value in {'J', 'Q', 'K'}:
				return 10
			elif self.face_value == 'A':
				return 11