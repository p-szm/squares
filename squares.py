#! /usr/bin/env python
__author__ = 'Patrick Szmucer'

from pyglet.gl import *
from pyglet.window import key
from UIboard import UIBoard
from board import Square
from move import Move

window = pyglet.window.Window(resizable=True)
margin = 20
glClearColor(1, 1, 1, 1)

# Define the moves
left = Move((-1,0), -1)
down = Move((0,-1), -1)
left_down = Move((-1,-1), -1)

b = UIBoard(20, (left, down, left_down))

@window.event
def on_draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()
	glTranslatef(window.width/2.0, window.height/2.0, 0)
	
	glPointSize(3)
	glColor3f(0, 0, 0)

	glBegin(GL_POINTS)
	glEnd()
	
	glLineWidth(1)
	b.render(window, margin)

@window.event
def on_mouse_press(x, y, button, mods):

	coords = b.coords(window, margin)
	min_x, min_y = coords[0]
	max_x, max_y = coords[1]

	x = x - window.width/2.0
	y = y - window.height/2.0

 	sq_size = (max_y-min_y)/(1.0*b.size)
 	m = int((x - min_x) / sq_size)
 	n = int((y - min_y) / sq_size)

 	val = b.get(m, n)
 	b.set(m, n, (val + 1)% 3)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ENTER:
    	b.solve()
    elif symbol == key.R:
    	b.reset()

@window.event
def on_resize(width, height):
	pass

pyglet.app.run()