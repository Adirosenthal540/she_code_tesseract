import cv2 as cv
import pytesseract
from matplotlib import pyplot as plt
from Image import Image
import sys
import numpy as np

WIDTH = 700
HEIGHT = 800
PIXEL_REMOVE = 20

def RotateImage():
    pass

def removePixelsEdge(img, numIdex):
    widthImg = img.shape[1]
    heightImg = img.shape[0]
    imgRemovePixels = img[numIdex:heightImg - numIdex, numIdex:widthImg - numIdex]
    imgResize = cv.resize(imgRemovePixels, (widthImg, heightImg))
    return imgResize

def FindLines(img):
    edges = cv.Canny(img, 50, 150, apertureSize=3)
    #edges = cv.Canny(gray, 50, 150, apertureSize=3)
    cv.imshow("edges",edges)
    cv.waitKey(0)
    lines = cv.HoughLinesP(edges,1,np.pi/180, 100, minLineLength=300, maxLineGap=20)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (0,255, 0), 2)

    cv.imshow("image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

# def click_event(event, x, y, flags, param):
#     if event == cv.EVENT_LBUTTONDOWN:
#         cv.circle(img, (x,y), 3, (0,0,255), -1)
#         points.append((x,y))
#         if len(points) >= 2:
#             cv.line(img, points[-1], points[-2], (255,0,0), 5)
#         cv.imshow("Select_area_of_text-need_to_be_a_square", img)
#
# def selectTextArea(img, points):
#     cv.imshow("Select_area_of_text-need_to_be_a_square", img)
#     cv.setMouseCallback("Select_area_of_text-need_to_be_a_square", click_event)
#     cv.imshow("Select_area_of_text-need_to_be_a_square", img)
#     cv.waitKey()
#     cv.destroyAllWindows()
#     if len(points)<4:
#         print( "ERROR - YOU NEED TO DROW SQUARE")
#         sys.exit()
#     points = np.array(points[0:4])
#     return points

def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), dtype=np.int32)
    add = myPoints.sum(1)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    return myPointsNew

def WropImag(img, points):
    imgContour = img.copy()
    points = reorder(points)
    width = img.shape[1]
    height = img.shape[0]
    pts1 = np.float32(points)  # PREPARE POINTS FOR WARP
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])  # PREPARE POINTS FOR WARP
    matrix = cv.getPerspectiveTransform(pts1, pts2)
    imgWarp = cv.warpPerspective(img, matrix, (width, height))
    imgWarp = removePixelsEdge(imgWarp, PIXEL_REMOVE)
    cv.imshow("wrop Image", imgWarp)
    cv.waitKey(0)
    return imgWarp

def main():
    global points
    points=[]
    img = cv.imread(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\test_images\unnamed1.jpg", 0)
    image = Image(img)

    image.resize(int((WIDTH / image.ImageWidth())*image.ImageWidth()), int((WIDTH / image.ImageWidth())*image.ImageHeight()))
    img = image.CopyImageArray()
    points = selectTextArea(img, points)

    print (type(image))
    print(image.ImageHeight())
    print(image.ImageWidth())
    imgWarp = WropImag(img, points)
    print(points)
    # img = cv.imread(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\test_images\test_tesseract.png", 0)
    #
    # cv.imshow("image",img)
    # cv.waitKey(0)
    # FindLines(img)