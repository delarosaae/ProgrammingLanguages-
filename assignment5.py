import sys
from CustomCanvas import CustomCanvasMaker
from rectpack import newPacker
from Rectangle import *
from tkinter import *

def pack(allRect, canvasSize):



	allRectangles = allRect
	print(allRectangles)

	listOfHeightAndWidth = [] * len(allRectangles)

	for aR in allRectangles:
		print(aR)
		heightOfRectObj = aR.getHeight()
		print(heightOfRectObj)

		widthOfRectObj = aR.getWidth()
		print(widthOfRectObj)

		heightandWidthInAList = [heightOfRectObj, widthOfRectObj]

		listOfHeightAndWidth.append(heightandWidthInAList)

	print(listOfHeightAndWidth)
	
	packer = newPacker()
	for r in listOfHeightAndWidth:
		packer.add_rect(*r)




	canvasSizeForBin = canvasSize
	bins = canvasSizeForBin
	height = canvasSizeForBin[0]
	width = canvasSizeForBin[1]
	#print(bins) prints out a tuple of the height of canvas and width

	packer.add_bin(height,width)
	packer.pack()

	nbins = len(packer)
	abin = packer[0]
	height = abin.height
	width = abin.width
	nrect = len(packer[0])
	print(nrect)


	rect = packer[0][0]
	x = rect.x
	y = rect.y
	w = rect.width
	h = rect.height

	print("below will show us where to put things in")


	CorrectVertex = [] * len(allRectangles)

	all_rects = packer.rect_list()
	for rect in all_rects:
		print(rect)
		b,x,y,w,h,rid = rect

		addAllTheVertex = [h,w,x,y]
		CorrectVertex.append(addAllTheVertex)

		#print(h)
		#print(w)
		#print(x)
		#print(y)
		#print(rid)
	print(CorrectVertex)




	#rectangleObjects = [] * len(rectangleCoordinates)
	#for y in rectangleCoordinates:
		#heightOfRectangle = y[0]
		#print(heightOfRectangle)
		#widthOfRectangle = y[1]
		#print(widthOfRectangle)
		#z = Rectangle(heightOfRectangle, widthOfRectangle, 0, 0)
		#rectangleObjects.append(z)
		#print(z.getHeight)


	

	returnRectObjects = [] * len(allRectangles)
	for changeObjects in CorrectVertex:
		finalHeigh = changeObjects[0]
		finalWidth = changeObjects[1]
		finalX	= changeObjects[2]
		finalY = changeObjects[3]

		addRectObj = Rectangle(finalHeigh, finalWidth, finalX, finalY)
		returnRectObjects.append(addRectObj)
	return (returnRectObjects)







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


		#get the second numberafter the comma
		secondNumString = x[x.index(",") + 1:]
		secondNumInt = int(secondNumString)
		#print(secondNumString)



		#make a list of them and add them to the list of vertex's
		cordinate = [firstNumInt, secondNumInt]
		allVertex.append(cordinate)



	#take a look at the list	
	print(allVertex)







	#now we will get the first two cordiniates for the canvas
	heightOfCanvas = allVertex[0][0]
	widthOfCanvas = allVertex[0][1]
	#take a look at the height of canvas and width
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



	#shows us how to get the height of the first rectangle object
	print(rectangleObjects[0].getHeight())






	#now create the canvas class and we might need to make a list of the heightOfCanvas and widthOfCanvas
	canvas = CustomCanvasMaker(heightOfCanvas, heightOfCanvas)
	tupleOfCanvasSize = (heightOfCanvas, widthOfCanvas)
	print(tupleOfCanvasSize)
	RectObjToPlaceInCanvas = pack(rectangleObjects, tupleOfCanvasSize)

	canvas.addRectangles(RectObjToPlaceInCanvas)