import numpy as np
import cv2
from GridClass import GridFrame

cap = cv2.VideoCapture(0)

#   I think I will need to create a custom class for my purposes
#   as well as a grid listener

<<<<<<< HEAD
#   Grid Frame Class that will serve as base for my project
#   It'll carry the frame and the Grid Listener
class GridFrame:
    def __init__(self, frame, cellSize):
        self.frame = frame
        self.cellSize = cellSize
        self.fHeight, self.fWidth, self.fChannels = frame.shape

        #   Array that later will hold the cells of the grid
        self.GridCells = []
        self.createGrid()

    #   Shows the frame that is held by the GridFrame
    def showGridFrame(self):
        cv2.imshow('frame',self.frame)

    #   Attempts to show A cell of the grid
    def showCell(self, cellNumber):
        self.GridCells[cellNumber].showC()

    #   Show all cells
    def showCells(self):
        for c in self.GridCells:
            c.showC()

    #   Also populates the GridCells Array that is a member of this class
    #   According to the cellSize specified on init
    def createGrid(self):
        cellHeight = int(self.fHeight/self.cellSize)
        cellWidth = int(self.fWidth/self.cellSize)
        for x in range(0,self.cellSize):
            for y in range(0, self.cellSize):
                # Create a new GridCell Instance and initialize
                cell = GridCell(cellHeight, cellWidth, cellHeight*y, cellWidth*x,
                                self.frame[cellHeight*y:cellHeight*y+cellHeight,cellWidth*x:cellWidth*x+cellWidth])
                self.GridCells.append(cell)

# Meta Object that will describe a singular cell in the GridFrame
# Will be used to find events occuring inside these cells
class GridCell():
    def __init__(self, height, width, startX, startY, partialFrame):
        self.height = height
        self.width = width
        self.startX = startX
        self.startY = startY
        self.partialFrame = partialFrame

    def showC(self):
        cv2.imshow('cell',self.partialFrame)

    # should create an overlay with an translucent color
    def drawBorders(self):
        # Color the border of each cell here
        x = 0


#Divides Image or frame into several images depending on subdivision rate
=======
### This is now Obsolete ### MIght be salvaged for other bits of Code ###
#   Divides Image or frame into several images depending on subdivision rate
>>>>>>> changes
def subdivide(frame, numOfSubFrms):
    #cloning the original frame such that we'll be working on a copy from now on
    frameC = np.array(frame, copy = True)

    # storing frame information such that we can do operations on it
    frameHeight, frameWidth, channels = frameC.shape
    #instantiate empty array that will hold the image cells later on
    imgCells = []

    # determining the cell size given the desired number of sub divisions
    cellHeight = int(frameHeight/numOfSubFrms)
    cellWidth = int(frameWidth/numOfSubFrms)

    cells = []
    # extracting cells from the frame copy
    for x in range(0,numOfSubFrms):
        for y in range(0, numOfSubFrms):
            imgCells.append(frameC[cellHeight*y:cellHeight*y+cellHeight,cellWidth*x:cellWidth*x+cellWidth])

    print(len(imgCells))
    for c in imgCells:
        cv2.imshow('cell',c)

    return imgCells



def colorMask(frame, lower, upper):
    # converting RGB to HSV
    # HSV standing for Hue, Saturation and Value (or aletrnatively Brightness)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of a specific color in HSV
    # in this case we define the range that the color blue takes up on the spectrum
    # the parameters given to the function are not R,G and B order
    # their order is B, G and R
    # in this case we are going from dark violet to cyan
    lower_bound = lower
    upper_bound = upper

    # threshold the HSV image to get only blue colors
    # what this means is that we removing all colors that are not in the specified inRange
    # we do that by applying a mask
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask = mask)
    return frame, mask, res

#   Method to time average run time of functions that are passed
#   Dunno how to use this yet lmao
#   average and counter should be passed as 0 and 1 respectively
def measureTime(average, counter, methodToTime):
    import time
    start = time.time()

    methodToTime()

    end = time.time()
    print(end - start)
    print("Execution time above ^^^")
    print("")
    time = end - start
    average += time
    counter += 1
    print("Average Time: ", average/counter, "Counter: ", counter)


# here we display the original frame alongside the mask that we created and the colorshifted picture
def show(frame, mask, res):
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

while(1):
    #frames, for the underscore notation see the followeing link
    # https://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python
    # in this case the underscore is used as a throwaway variable which stores the retval value returned by the read function
    # as I understand it, historically, the underscore is used to indicate that part of the result of a function is being deliberately ignored
    _, frame = cap.read()

    #https://dsp.stackexchange.com/questions/2687/why-do-we-use-the-hsv-colour-space-so-often-in-vision-and-image-processing
    # I should look into using a hsv colorspace instead, it seems more useful than rgb in this specific case
    colorDict = {
        'blue':[[86, 31, 4], [220, 88, 50]],
        'red':[[17, 15, 100], [50, 56, 200]],
        'yellow':[[25, 146, 190], [62, 174, 250]],
        'gray':[[103, 86, 65], [205, 133, 188]]
        }
    lower_bound = np.array(colorDict['gray'][0])
    upper_bound = np.array(colorDict['gray'][1])

    image, mask, res = colorMask(frame, lower_bound, upper_bound)
    #show(image, mask, res)

    #subdivide(frame, 2)

<<<<<<< HEAD
    GF = GridFrame(frame,2)
    GF.showGridFrame()
    GF.showCells()
=======
    GF = GridFrame(frame,3)

    GF.showGridFrame()

    GF.showCells()

    GF.drawCellBorders()

    GF.drawGrid()
>>>>>>> changes

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
