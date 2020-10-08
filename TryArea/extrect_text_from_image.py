import cv2
import pytesseract
from matplotlib import pyplot as plt
import numpy as np
pytesseract.pytesseract.tesseract_cmd =  r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\handwriteDoc\train_songs\testPDF\316550797_0_2.tif", 0)
cv2.imshow("img",img )
cv2.waitKey(0)
"""
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#print(pytesseract.image_to_string(img))
_, binary_thresh = cv2.threshold(img, 120,255, cv2.THRESH_BINARY_INV)

kernal = np.ones((2,2), np.uint8)
dilation = cv2.dilate(binary_thresh, kernal , iterations=1)
erosion = cv2.erode(binary_thresh, kernal, iterations=2)
#th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 22)


ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("number of contuers:"+str(len(contours)))
img_copy = np.array(img[:])
drawContours = cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 1)
_, thresh_drawContours = cv2.threshold(drawContours, 127, 255, cv2.THRESH_BINARY_INV)

titles = ["image", "binary_thresh", "dilation","erosion", "find contours"]
images = [img, binary_thresh, dilation, erosion, thresh_drawContours]


for i in range(5):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()




cv2.waitKey(0)
cv2.destroyAllWindows()
"""
# lines = cv2.HoughLinesP(binary_thresh,1,np.pi/180, 100, minLineLength=300, maxLineGap=20)
# print(lines)
# angle = 0
# for line in lines:
#     x1, y1, x2, y2 = line[0]
#     r = np.arctan2(y1-y2, x2-x1)
#     angle += np.arctan2(y2-y1,x2-x1)
# avg_radian = angle / len(lines)
# avg_angle = avg_radian * 180 / np.pi
# hImg, wImg,_= img.shape
# boxes = pytesseract.image_to_data((img))
# print (boxes)
"""
str= pytesseract.image_to_string(binary_thresh, lang="heb")
str= pytesseract.image_to_string(dilation, lang="heb")
str= pytesseract.image_to_string(drawContours, lang="heb")
print (str)
"""
str= pytesseract.image_to_string(img, lang="heb")
print ([str])
# boxes= pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     print(b)
#     b=b.split(" ")
#     x,y,w,h = int(b[1]),int(b[2]), int(b[3]),int(b[4])
#     cv2.rectangle(img, (x,hImg-y), (w,hImg -h), (0,0,255), 1)
# cv2.imshow('Result', img)
# cv2.waitKey(0)
