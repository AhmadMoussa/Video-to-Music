import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# def subdivide(frame, numOfSubFrms):
#    imgCells = []
#    xRange = (frame.shape[0]/numOfSubFrms)
#    for x in range(xRange)

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

    lower_bound = np.array([110,50,50])
    upper_bound = np.array([255, 173, 96])

    image, mask, res = colorMask(frame, lower_bound, upper_bound)
    show(image, mask, res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
     break

cv2.destroyAllWindows()
