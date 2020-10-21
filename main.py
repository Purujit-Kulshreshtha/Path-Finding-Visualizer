import pygame

#make window
WIDTH = 800
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
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

	def is_nothing(self):
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

	def reset(self):
		self.color = WHITE

	def draw(self, window):
		pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

	def update_nbrs(self, grid):
		self.nbrs = []

		#check and add nbr DOWN current node
		if self.row < self.total_rows - 1 and not grid[self.row+1][self.col].is_barrier():
			self.nbrs.append(grid[self.row+1][self.col])

		#check and add nbr UP current node
		if self.row < 0 and not grid[self.row-1][self.col].is_barrier():
			self.nbrs.append(grid[self.row+1][self.col])

		##check and add nbr RIGHT current node
		if self.col < self.total_rows - 1 and not grid[self.row][self.col+1].is_barrier():
			self.nbrs.append(grid[self.row][self.col+1])

		#check and add nbr RIGHT current node
		if self.col < 0 and not grid[self.row][self.col-1].is_barrier():
			self.nbrs.append(grid[self.row][self.col-1])

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

#draw grid on window
def draw_grid(window, rows, width):
	gap = width//rows
	for i in range(0, rows):
		pygame.draw.line(window, GREY, (0, i*gap), (width, i*gap))
		for j in range(0, rows):
			pygame.draw.line(window, GREY, (j*gap, 9), (j*gap, width))

#draw everything
def draw(window, grid, rows, width):
	window.fill(WHITE)

	for row in grid:
		for block in row:
			block.draw(window)

	draw_grid(window, rows, width)
	pygame.display.update()

#getting the mouse position
def get_clicked_pos(pos, rows, width):
	gap = width//rows
	y, x = pos
	row = y//gap
	col = x//gap

	return row, col

#mainloop for window
def main(window, width):
	#variables
	ROWS = 50
	grid = make_grid(ROWS, width)

	start = None
	end = None

	run = True
	started = False

	#mainloop
	while run:
		draw(window, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if started:
				continue

			#checks for left-click
			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				block = grid[row][col]

				#check if there's a start position
				if not start and block != end:
					start = block
					start.make_start()

				#checks if there's an end position
				elif not end and block != start:
					end = block
					end.make_end()

				elif block != start and block != end:
					block.make_bar()

			#checks for right-click
			elif pygame.mouse.get_pressed()[2]:
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				block = grid[row][col]
				block.reset()

				if block == start:
					start = None

				elif block == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and not started:
					pass 


	pygame.quit()


main(WINDOW, WIDTH)