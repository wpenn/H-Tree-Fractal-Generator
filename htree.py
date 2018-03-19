from drawingpanel import *
panel = DrawingPanel(500, 500)
canvas = panel.canvas

def draw_htree(n):
	'''n denotesthe recursive depth'''
	draw_htree_rec_helper(n, 200, 250, 250)

def drawh(size, x, y):
	canvas.create_line(x - size/2, y - size/2, x - size/2, y + size/2, activefill="green") #left
	canvas.create_line(x - size/2, y, x + size/2, y, activefill="yellow") #center
	canvas.create_line(x + size/2, y - size/2, x + size/2, y + size/2, activefill="blue") #right

def draw_htree_rec_helper(n, size, x, y):
	'''draw htree that is centered at (x,y) 
	of height = width = size '''
	if n == 1:
		#draw a single H
		drawh(size, x, y)
		return
	
	drawh(size, x, y)

	draw_htree_rec_helper(n - 1, size/2, x - size/2, y + size/2) #top left
	draw_htree_rec_helper(n - 1, size/2, x - size/2, y - size/2) #bottom left
	draw_htree_rec_helper(n - 1, size/2, x + size/2, y + size/2) #top right
	draw_htree_rec_helper(n - 1, size/2, x + size/2, y - size/2)


def main():
	draw_htree(int(input("How many iterations? ")))

main()