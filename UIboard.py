from board import Board, Square
from pyglet.gl import *

class UIBoard(Board):
	def __init__(self, size, moves, one_by_one=False):
		Board.__init__(self, size, moves, one_by_one)

	def render(self, window, margin):

		coords = self.coords(window, margin)
		min_x, min_y = coords[0]
		max_x, max_y = coords[1]

		sq_size = (max_y-min_y)/(1.0*self.size)

		glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
		glBegin(GL_LINES)
		for i in range(self.size+1):
			glVertex2f(min_x + i*sq_size, min_y)
			glVertex2f(min_x + i*sq_size, max_y)

			glVertex2f(min_x, min_y + i*sq_size)
			glVertex2f(max_x, min_y + i*sq_size)
		glEnd()

		for i in range(self.size):
			for j in range(self.size):
				val = self.get(i, j)
				if val == Square.WillWin:
					glColor3f(0.3, 0.8, 0.3)
				elif val == Square.WillLose:
					glColor3f(1, 0.8, 0.8)
				elif val == Square.Win:
					glColor3f(0, 0.5, 0)
				elif val == Square.Lose:
					glColor3f(1, 0, 0)
				else:
					glColor3f(1, 1, 1)

				glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
				glBegin(GL_QUADS)

				glVertex2f(min_x + (i+0.2)*sq_size, min_y + (j+0.2)*sq_size)
				glVertex2f(min_x + (i+0.2)*sq_size, min_y + (j+0.8)*sq_size)
				glVertex2f(min_x + (i+0.8)*sq_size, min_y + (j+0.8)*sq_size)
				glVertex2f(min_x + (i+0.8)*sq_size, min_y + (j+0.2)*sq_size)

				glEnd()

	def coords(self, window, margin):
		max_y = window.height/2.0 - margin
		min_y = -max_y
		max_x = window.width/2.0 - margin
		min_x = -max_x

		if max_x > max_y:
			max_x = max_y
			min_x = min_y
		else:
			max_y = max_x
			min_y = min_x

		return ((min_x, min_y), (max_x, max_y))