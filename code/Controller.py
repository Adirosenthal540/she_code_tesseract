from ImageProcessing import ImageProcessing
from HandwrittenDoc import Check_image_page, ExportHandriteLinesFromScannedDoc
import DataManager
import ModelTesseract
import Main
from tkinter import messagebox
import cv2 as cv
import sys
import numpy as np
from matplotlib import pyplot as plt
import os

class Controller():

    def __init__(self, isTrain, images, root, isScanned = False):
        self.isTrain = isTrain
        self.isScanned = isScanned
        self.image_processing_list = images
        self.root = root

    def processLabeledImages(self):
        newImagesForTrain = []
        image = self.images[0]
        boundries = ImageProcessing.GetLineBounds(image .imageArray)
        line_images_array = []
        for i in range(len(boundries)):
            x, y, w, h = boundries[i]
            cutImage = image.cutImage(image.imageArray, x, y, x + w, y + h)
            line_images_array.append(cutImage)

        newImagesArrayForTrain = Main.userSetLabel(line_images_array)
        newImagesForTrain.append(ImageProcessing(cutImage, imagePath=None, Label=Label, handwrite_ID=image.handwrite_ID))

        numS, numE = DataManager.Insert_to_database(newImagesForTrain)
        return (numS, numE)
    # def processLabeledImages(self):
    #     newImagesForTrain = []
    #     for image in self.image_processing_list:
    #         boundries = ImageProcessing.GetLineBounds(image.imageArray)
    #         print(boundries)
    #         print(len(boundries))
    #         text = image.Label
    #         lines = text.split('\n')
    #         lines_text = []
    #         num_lines = 0
    #         for line in lines:
    #             if line != "":
    #                 num_lines += 1
    #                 lines_text.append(line)
    #         #print(num_lines)
    #
    #         if (num_lines == len(boundries)):
    #             for i in range(len(boundries)):
    #                 x, y, w, h = boundries[i]
    #                 cutImage = image.cutImage(image.imageArray, x, y, x + w, y + h)
    #                 Label = lines[i]
    #                 newImagesForTrain.append(ImageProcessing(cutImage, imagePath=None, Label=Label, handwrite_ID=image.handwrite_ID))
    #         else:
    #             #return "The text of image "+ os.path.basename(image.imagePath) + " doesnt match to his text file"
    #             message = "The text of image "+ os.path.basename(image.imagePath) + " doesnt match to his text file"
    #             messagebox.showerror("ERROR", message)
    #             print(message)
    #     numS, numE = DataManager.Insert_to_database(newImagesForTrain)
    #     return (numS, numE)

    def processScannedImages(self):
        newImagesForTrain =[]
        for image in self.image_processing_list:
            pageNum = Check_image_page(image.imagePath)
            newImagesForTrain= newImagesForTrain + ExportHandriteLinesFromScannedDoc(image, pageNum)
        numS, numE = DataManager.Insert_to_database(newImagesForTrain)
        return (numS, numE)

    def processLabeledImages(self):
        pass

    def processExportFromImage(self):
        tesseract = ModelTesseract.ModelTesseract()
        text = tesseract.ExportTextTesseract(self.image_processing_list[0].imageArray)
        # cv.imshow("hhhh",self.image_processing_list[0].imageArray)
        # cv.waitKey(0)
        return text

    def main(self):
        for image in self.image_processing_list:
            print(image.imagePath)
            print(image.Label)
            print(image.handwrite_ID)

        if self.isTrain:
            if self.isScanned:
                numS, numE = self.processScannedImages()
                return ("Sucsses - insert " +str(numE - numS)+ " lines for training, images - " + str(numS) + " to "+str(numE))
            else:
                self.processLabeledImages()
        else:
            text = self.processExportFromImage()
            return text