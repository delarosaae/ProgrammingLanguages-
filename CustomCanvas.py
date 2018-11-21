from tkinter import *
from Rectangle import *

window = Tk()


class CustomCanvasMaker: 
	def __init__(self, height, width):
		self.height = height 
		self.width = width
		global canvas 
		canvas = Canvas(window, height=self.height, width=self.width)

		crect = canvas.create_rectangle(0, 50, 0, 50, outline="black")

		canvas.pack()
		window.mainloop()

	def addRectangles(self, allRect):
		self.allRect = allRect

		allRect2 = self.allRect

		for allRectCoord in allRect2:
			#print(aR)
			heightOfRectObj = allRectCoord.getHeight()
			print(heightOfRectObj)

			widthOfRectObj = allRectCoord.getWidth()
			print(widthOfRectObj)

			x = allRectCoord.getX()
			y = allRectCoord.getY()

			#heightandWidthInAList = [heightOfRectObj, widthOfRectObj, x, y]
			#crect = canvas.create_rectangle(x, heightOfRectObj, y, widthOfRectObj)
			
