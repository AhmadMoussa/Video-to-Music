import cv2
import numpy as np
from CellClass import GridCell
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

    #   Show all cells in different windows
    def showCells(self):
        # Calling an enumerator on the gridcells because we will need a counter to label the pictures accordingly
        for i, c in enumerate(self.GridCells):
            c.showC(i)

    #   Draw a Grid overlayed ontop of the actual image
    #   Average Time:  0.0020421147819925057 Counter:  1259
    def drawGrid(self):
        #   Create the overlay
        blank_image = np.zeros((self.fHeight,self.fWidth,3), np.uint8)
        for c in self.GridCells:
            cv2.rectangle(blank_image,(c.startY,c.startX),(c.startY+c.width,c.startX+c.height),(255,255,255),1,8,0)

        cv2.imshow("grid",blank_image)

    #   Average Time:  0.002263623596685618 Counter:  1235
    #   A tad bit slower that the other function hence drawGrid() method will be preferred for now
    # Unless other complications occur
    def drawCellBorders(self):
        blank_image = np.zeros((self.fHeight,self.fWidth,3), np.uint8)
        for c in self.GridCells:
            c.drawBorders(blank_image)
        cv2.imshow('borders',blank_image)



    #   Populates the GridCells Array that is a member of this class
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
