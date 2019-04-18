import numpy as np
import cv2

# Meta Object that will describe a singular cell in the GridFrame
# Will be used to find events occuring inside these cells
class GridCell():
    def __init__(self, height, width, startX, startY, partialFrame):
        self.height = height
        self.width = width
        self.startX = startX
        self.startY = startY
        self.partialFrame = partialFrame

    def showC(self,i):
        # Using a string formatter to label the pictures differently for them to show
        # openCV imshow() windows need different labels to appear on screen
        cv2.imshow("cell{}".format(i),self.partialFrame)

    # should create an overlay with an translucent color
    def drawBorders(self, blank_image):
        # Color the border of each cell here
        cv2.rectangle(blank_image,(self.startY,self.startX),(self.startY+self.width,self.startX+self.height),(255,255,255),1,8,0)
