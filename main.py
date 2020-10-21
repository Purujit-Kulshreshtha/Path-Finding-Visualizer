import pygame

#make window
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding Visualzier")

#global variables - colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

#close for each block
class block_class():
	#Initialization
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row*width
		self.y = col*width
		self.color = WHITE
		self.nbrs = []
		self.width = width
		self.total_rows = total_rows

		############ checks the status of the block ##############

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == RED

	def is_open(self):
		return self.color == GREEN

	def is_bar(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == ORANGE

	def is_end(self):
		return self.color == TURQUOISE

	def reset(self):
		return self.color == WHITE

		########### modifies status of block #############
	
	def make_closed(self):
		 self.color = RED

	def make_open(self):
		 self.color = GREEN

	def make_bar(self):
		 self.color = BLACK

	def make_start(self):
		 self.color = ORANGE

	def make_end(self):
		 self.color = TURQUOISE

	def make_path(self):
		self.color = PURPLE

	def draw(self, window):
		pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

	def update_nbrs(self, grid):
		pass

	############ compares with other block #############

	def __lt__(self, other):
		return False

#finds distance between two points
def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	distance = abs(x1-x2) + abs(y1-y2)
	return distance

#makes the grid in the form of a 2-D list
def make_grid(rows, width):
	gap = width//rows
	grid = []
	for i in range(0, rows):
		grid.append([])
		for j in range(0, rows):
			spot = block_class(i, j, gap, rows)
			grid[i].append(spot)

	return grid



