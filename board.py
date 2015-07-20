import numpy

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

Square = enum('Empty', 'Win', 'Lose', 'WillWin', 'WillLose')

class Board:
	def __init__(self, size, moves, one_by_one=False):
		self.size = size
		self.moves = moves
		self.data = numpy.empty((self.size, self.size))
		self.data[:] = Square.Empty
		self.one_by_one = one_by_one
		self.locked = False

	def get(self, x, y):
		if x > self.size-1 or y > self.size-1 or x < 0 or y < 0:
			return None
		else:
			return self.data[x][y]

	def set(self, x, y, val):
		if self.locked or x > self.size-1 or y > self.size-1 or x < 0 or y < 0:
			return False
		else:
			self.data[x][y] = val
			return True

	def solve(self):
		
		corner = self.get(0, 0)
		if corner not in (Square.Win, Square.Lose):
			print 'No action specified for lower left corner'
			return

		self.lock()

		for i in range(self.size):
			for j in range(self.size):
				if  not self.get(i, j) == Square.Empty:
					continue

				vals = []
				for move in self.moves:
					if move.limit == -1:
						lim = self.size
					else:
						lim = move.limit

					for k in range(lim+1)[1:]:
						val = self.get(i+k*move.x, j+k*move.y)
						if val:
							vals.append(val)
						else:
							break

				if Square.Win in vals or Square.WillWin in vals:
					self.data[i, j] = Square.WillLose
				elif all(x in (Square.Lose, Square.WillLose) for x in vals):
					self.data[i, j] = Square.WillWin

	def reset(self):
		self.data = numpy.zeros((self.size, self.size))
		self.unlock()

	def lock(self):
		self.locked = True

	def unlock(self):
		self.locked = False




