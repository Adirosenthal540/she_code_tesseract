import cv2
import numpy as np
from matplotlib import pyplot as plt
import utlis

def click_event(event, x, y, flags, param):
    if event ==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255,0,0), 5)
        cv2.imshow("Image", img)

def selectTextArea(img):
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", click_event)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return points
########################################################################
pathImage = r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\test_images\unnamed7.jpg"

heightImg = 500
widthImg = 480
########################################################################

utlis.initializeTrackbars()
count = 0


img = cv2.imread(pathImage)
img = cv2.resize(img, (widthImg, heightImg))  # RESIZE IMAGE
imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)  # CREATE A BLANK IMAGE FOR TESTING DEBUGING IF REQUIRED
imgWarpColored=imgBlank
imgWarpGray=imgBlank
imgAdaptiveThre=imgBlank
imgContour = img.copy()

points = []
points = selectTextArea(img)
points = np.array(points[0:4])

if points.size != 0:
    points = utlis.reorder(points)
    cv2.drawContours(imgContour, points, -1, (0, 255, 0), 20)  # DRAW THE BIGGEST CONTOUR
    cv2.imshow("Image", img)
    cv2.waitKey()
    imgContour = utlis.drawRectangle(imgContour, points, 2)
    pts1 = np.float32(points)  # PREPARE POINTS FOR WARP
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])  # PREPARE POINTS FOR WARP
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    cv2.imshow("Image", imgWarpColored)
    cv2.waitKey()

    img = imgWarpColored
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # CONVERT IMAGE TO GRAY SCALE
    _, binary_thresh = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)

    kernal = np.ones((2, 2), np.uint8)
    dilation = cv2.dilate(binary_thresh, kernal, iterations=1)
    erosion = cv2.erode(binary_thresh, kernal, iterations=2)
    # th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 22)

    ret, thresh = cv2.threshold(img, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("number of contuers:" + str(len(contours)))
    img_copy = np.array(img[:])
    drawContours = cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 1)
    _, thresh_drawContours = cv2.threshold(drawContours, 127, 255, cv2.THRESH_BINARY_INV)

    titles = ["image", "binary_thresh", "dilation", "erosion", "find contours"]
    images = [img, binary_thresh, dilation, erosion, thresh_drawContours]

    for i in range(5):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #
    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # CONVERT IMAGE TO GRAY SCALE
    # imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)  # ADD GAUSSIAN BLUR
    # thres = utlis.valTrackbars()  # GET TRACK BAR VALUES FOR THRESHOLDS
    # imgThreshold = cv2.Canny(imgBlur, thres[0], thres[1])  # APPLY CANNY BLUR
    # cv2.imshow("Image", imgThreshold)
    # cv2.waitKey()
    # # kernel = np.ones((5, 5))
    # # imgDial = cv2.dilate(imgThreshold, kernel, iterations=2)  # APPLY DILATION
    # # imgThreshold = cv2.erode(imgDial, kernel, iterations=1)  # APPLY EROSION
    #
    #
    # # # REMOVE 20 PIXELS FORM EACH SIDE
    # # imgWarpColored = imgWarpColored[20:imgWarpColored.shape[0] - 20, 20:imgWarpColored.shape[1] - 20]
    # # imgWarpColored = cv2.resize(imgWarpColored, (widthImg, heightImg))
    #
    # # APPLY ADAPTIVE THRESHOLD
    # imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
    #
    # # _, mask = cv2.threshold(imgWarpGray, 220, 225, cv2.THRESH_BINARY_INV)
    # imgAdaptiveThre = cv2.adaptiveThreshold(imgWarpGray, 255, 1, 1, 7, 2)
    # imgAdaptiveThre = cv2.bitwise_not(imgAdaptiveThre)
    # imgAdaptiveThre = cv2.medianBlur(imgAdaptiveThre, 3)
    #
    # # Image Array for Display
    # imageArray = ([img, imgGray, imgThreshold, imgContour],[imgContour, imgWarpColored, imgWarpGray, imgAdaptiveThre])
    #
    # # LABELS FOR DISPLAY
    # lables = [["Original", "Gray", "Threshold", "Contours"],["Biggest Contour", "Warp Prespective", "Warp Gray", "Adaptive Threshold"]]
    #
    # stackedImage = utlis.stackImages(imageArray, 0.75, lables)
    # cv2.imshow("Result", stackedImage)
    # cv2.imshow
    # cv2.waitKey()
    # # SAVE IMAGE WHEN 's' key is pressed
    # if cv2.waitKey(1) & 0xFF == ord('s'):
    #     cv2.imwrite("Scanned/myImage" + str(count) + ".jpg", imgWarpColored)
    #     cv2.rectangle(stackedImage, ((int(stackedImage.shape[1] / 2) - 230), int(stackedImage.shape[0] / 2) + 50),
    #                   (1100, 350), (0, 255, 0), cv2.FILLED)
    #     cv2.putText(stackedImage, "Scan Saved", (int(stackedImage.shape[1] / 2) - 200, int(stackedImage.shape[0] / 2)),
    #                 cv2.FONT_HERSHEY_DUPLEX, 3, (0, 0, 255), 5, cv2.LINE_AA)
    #     cv2.imshow('Result', stackedImage)
    #     cv2.waitKey(300)
    #     count += 1