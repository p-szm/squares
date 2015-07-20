class Move:
	def __init__(self, direction, limit=-1):
		self.x = direction[0]
		self.y = direction[1]
		self.limit = limit