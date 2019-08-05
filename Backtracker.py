from tkinter import *
from numpy import random as rand
#	VARIABLES
root = Tk().title("Laberinto")
FRAME = 50
w = 100
width = 500
height = 500
grid = []
stack = []
cols = width//w
rows = height//w

c = Canvas(root, width=width, height=height, bg="#555")
c.grid(row=0, column=0)

def setup():
	global cols, rows, current

	for j in range(rows):
		for i in range(cols):
			cell = Cell(i, j)
			grid.append(cell)
	
	current = grid[0]
	stack.append(current)


def draw():
	global current, stack
	for i in range(len(grid)):
		grid[i].show()
	# Etapa 1
	current.visited = True
	current.show()
	n_cell = current.checkNeighbors()
	if hasattr(n_cell, 'visited'):
		n_cell.visited = True
		# Etapa 2
		stack.append(n_cell)
		# Etapa 3
		removeWalls(current, n_cell)
		# Etapa 4
		current = n_cell
		c.after(FRAME, draw)
	elif len(stack)>0:
		current = stack.pop()
		c.after(FRAME, draw)


def removeWalls(a, b):
	x = a.i-b.i
	y = a.j-b.j
	if x==1:
		a.walls[3] = False
		b.walls[1] = False
	elif x==-1:
		a.walls[1] = False
		b.walls[3] = False
	if y==1:
		a.walls[0] = False
		b.walls[2] = False
	elif y==-1:
		a.walls[2] = False
		b.walls[0] = False

def index(i, j):
	if (i<0 or j<0):
		return -1
	elif  (i>cols-1 or j>rows-1):
		return -1
	return i+j*cols


class Cell():
	global c, w

	def __init__(self, i, j):
		self.i = i
		self.j = j
		self.walls = [True, True, True, True]
		self.visited = False
	
		

	def show(self):
		
		x = self.i*w
		y = self.j*w
		if self.visited:
			c.create_polygon(x,y,x+w,y,x+w,y+w,x,y+w, fill="red", outline="", width=2)
		if self.walls[0]:	#------------------->	MURO SUPERIOR
			c.create_line(x, y, x + w, y, width=3)
		if self.walls[1]:	#------------------->	MURO DERECHO
			c.create_line(x + w, y, x + w, y + w, width=3)
		if self.walls[2]:	#------------------->	MURO INFERIOR
			c.create_line(x + w, y + w, x,y + w, width=3)
		if self.walls[3]:	#------------------->	MURO IZQUIERDO
			c.create_line(x, y + w, x, y, width=3)
		current.highlight()
	
	def highlight(self):
		x = self.i*w
		y = self.j*w
		c.create_polygon(x,y,x+w,y,x+w,y+w,x,y+w, fill="green", outline="", width=2)

	def checkNeighbors(self):
		neighbors 	= []

		top 	= grid[index(self.i,self.j-1)]
		right 	= grid[index(self.i+1,self.j)]
		bottom 	= grid[index(self.i,self.j+1)]
		left	= grid[index(self.i-1,self.j)]

		if (index(self.i,self.j-1)!=-1 and not top.visited):		#------------------->	MURO SUPERIOR
			neighbors.append(top)
		if (index(self.i+1,self.j)!=-1 and not right.visited):	#------------------->	MURO SUPERIOR
			neighbors.append(right)
		if (index(self.i,self.j+1)!=-1 and not bottom.visited):	#------------------->	MURO SUPERIOR
			neighbors.append(bottom)
		if (index(self.i-1,self.j)!=-1 and not left.visited):		#------------------->	MURO SUPERIOR
			neighbors.append(left)
		
		if len(neighbors)>0:
			r = rand.randint(0,len(neighbors))
			return neighbors[r]
		else:
			return None


setup()
draw()
mainloop()