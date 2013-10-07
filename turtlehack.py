import turtle
import random

# A function that takes a radius, a color, and an optional thickness and draws a circle
#def colored_circle(radius, color, thickness = 1):
	# TODO: write this function 


# A function that takes a side length and a color and makes a square. 
#ef colored_square(side_length, color):
	# TODO: write this function 

# A function that takes a number and makes that many random sized circles
#def random_circle(number_of_circles):
	# TODO: write this function

# A function that changes the turtle's color to a random color
def random_color():
	'''
	returns a random hex value
	'''
	color_value = str(hex(random.randint(0000000,16777215)))
	color_value = color_value[2:]
	if len(color_value) <6:
		color_value = (6-len(color_value))*'0' + color_value
	return "#" +color_value

# A function that takes a number and sets the turtle to a random location from x to -x and y to -y
#def random_location():
	# TODO: write this function 
