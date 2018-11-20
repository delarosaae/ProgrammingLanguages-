from tkinter import *

window = Tk()

class CustomCanvasMaker: 
	def __init__(self, height, width):
		self.height = height 
		self.width = width
		canvas = Canvas(window, height=self.height, width=self.width)
		canvas.pack()
		window.mainloop()
