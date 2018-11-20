import sys
from CustomCanvas import CustomCanvasMaker

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
	print(heightOfCanvas)

	rectangleCoordinates = allVertex[1::]
	print(rectangleCoordinates)

	#now create the canvas class and we might need to make a list of the heightOfCanvas and widthOfCanvas
	canvas = CustomCanvasMaker(heightOfCanvas, heightOfCanvas)