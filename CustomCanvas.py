from tkinter import *
from Rectangle import *

window = Tk()



class CustomCanvasMaker: 
	def __init__(self, height, width, allRect):
		self.height = height 
		self.width = width 
		
		#create the canvas with the correct height and width
		canvas = Canvas(window, height=self.height, width=self.width, bg="blue")

		self.allRect = allRect


		allRect2 = self.allRect
		

		for allRectCoord in allRect2:
			# this will get all the height, width, x, and y from each of our rectangles
			heightOfRectObj = allRectCoord.getHeight()
			widthOfRectObj = allRectCoord.getWidth()
			x = allRectCoord.getX()
			y = allRectCoord.getY()

			#the bottom print calls are just to make sure that I was getting what I needed
			#print(x)
			#print(y)
			#print(heightOfRectObj)
			#print(widthOfRectObj)
			#heightandWidthInAList = [heightOfRectObj, widthOfRectObj, x, y]
			
			#this will place the rectangles in the canvas
			canvas.create_rectangle(x, y, heightOfRectObj + x, widthOfRectObj + y, outline="black")
			


		
		canvas.pack()
		window.mainloop()
	


		#this class will be called to get the rectangles and add them to the canvas
	def addRectangles(self, allRect):
		self.allRect = allRect
		##self.canvas = canvas

		allRect2 = self.allRect

		for allRectCoord in allRect2:
			#pWill get the all the rectangle to place on canvas
			heightOfRectObj = allRectCoord.getHeight()
			

			widthOfRectObj = allRectCoord.getWidth()
#			print(widthOfRectObj)

			x = allRectCoord.getX()
			y = allRectCoord.getY()

			
			x = self.canvas.create_rectangle(x, y, heightOfRectObj + x, widthOfRectObj + y, outline="black")


