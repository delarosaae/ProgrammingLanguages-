import sys
from CustomCanvas import CustomCanvasMaker
from rectpack import newPacker
from Rectangle import *


def pack(allRect, canvasSize):
	allRectangles = allRect
	print(allRectangles)
	canvasSizeForBin = canvasSize
	packer = newPacker()
	for r in allRectangles:
		packer.add_rect(*r)

	bins = canvasSizeForBin
	height = canvasSizeForBin[0]
	width = canvasSizeForBin[1]
	print("Where the pack is")
	print(bins)

	packer.add_bin(height,width)
	packer.pack()

	nbins = len(packer)
	abin = packer[0]
	height = abin.height
	width = abin.width
	nrect = len(packer[0])
	print(nrect)

if __name__ == "__main__":
	#got a list object named files that contains the lines of the text file
	#we now have string literals, so we will need to parse them and make them int
	with open(sys.argv[1], 'r') as file:
		files = [line.strip() for line in file]
	#print(files)

	#make a list inside of a list where the inside list contains the the coordinates
	#but first we make a list that has the number of spots that our file has
	allVertex = [] * len(files)
	
	#now, we will loop the list files object and make
	for x in files:
		#get the first number before the comma
		firstNumString = x[:x.index(",")]
		firstNumInt = int(firstNumString)
		secondNumString = x[x.index(",") + 1:]
		secondNumInt = int(secondNumString)
		#print(secondNumString)
		cordinate = [firstNumInt, secondNumInt]
		allVertex.append(cordinate)
	print(allVertex)

	#now we will get the first two cordiniates for the canvas
	heightOfCanvas = allVertex[0][0]
	widthOfCanvas = allVertex[0][1]
	print(heightOfCanvas)
	print(widthOfCanvas)

	#A list of the rectangle cordinates 
	rectangleCoordinates = allVertex[1::]
	print(rectangleCoordinates)

	#now create the Rectangle objects for each rectangle coordinate

	rectangleObjects = [] * len(rectangleCoordinates)
	for y in rectangleCoordinates:
		heightOfRectangle = y[0]
		#print(heightOfRectangle)
		widthOfRectangle = y[1]
		#print(widthOfRectangle)
		z = Rectangle(heightOfRectangle, widthOfRectangle, 0, 0)
		rectangleObjects.append(z)
		#print(z.getHeight)

	print(rectangleObjects[0].getHeight())


	#now create the canvas class and we might need to make a list of the heightOfCanvas and widthOfCanvas
	#canvas = CustomCanvasMaker(heightOfCanvas, heightOfCanvas)
	tupleOfCanvasSize = (heightOfCanvas, widthOfCanvas)
	print(tupleOfCanvasSize)
	pack(rectangleObjects, tupleOfCanvasSize)

	