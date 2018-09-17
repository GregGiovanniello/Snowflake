"""
program: snowflake.py
author: Greg

this program will draw a koch snowflake pattern using turtle graphics. input level of the snowflake will be given by the user

"""

from turtle import Turtle

def drawKoch(width, height, size, level):
	t = Turtle()
	t.up()
	t.goto(-width, height)
	t.down()
	drawFractalLine(t, size, 0, level)
	drawFractalLine(t, size, -120, level)
	drawFractalLine( t, size, 120, level)
	
def drawFractalLine(t, size, angle, level):
	if (level == 0):
		t.setheading(angle)
		t.forward(size)
	else:
		drawFractalLine(t, size // 3,angle, level - 1)
		drawFractalLine(t, size // 3,angle + 60, level - 1)
		drawFractalLine(t, size // 3,angle - 60, level - 1)
		drawFractalLine(t, size // 3,angle , level - 1)
		
def main():
	width = int(input("Enter the snowflake width: "))
	height = int(input("Enter the height of the snowflake: "))
	size = int(input("Enter the numeric size of the snowflake: "))
	level = int(input("Enter the snowflake level: "))
	drawKoch(width, height, size, level)
	input("Press ENTER to END the program")
	
if __name__ == "__main__":
	main()