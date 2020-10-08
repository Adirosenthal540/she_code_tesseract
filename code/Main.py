import Controller
import ImageProcessing
import HandwrittenDoc
import DataManager
#from DataManager import check_database
import cv2 as cv
from PIL import Image
import sys, numpy as np
from matplotlib import pyplot as plt
import os, math
from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
from pdf2image.exceptions import PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError

def Status_program(i):
    switcher={
        0: "Create data" ,
        1: "Extract text" ,
        }
    return switcher.get(i, " ")

def maessage_type(i):
    switcher={
        0: "information" ,
        1: "warning" ,
        2: "error"
        }
    return switcher.get(i, " ")

def insertDocuments(i):
    switcher={
        "Scanned":0  ,
        "Labeled":1 ,
        }
    return switcher.get(i, " ")

HELP_TEXT_DOC_CREATE = r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\code\help_create.txt"
HELP_TEXT_DOC_EXTRACT = r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\code\help_extract.txt"
IMAGE_WIDTH_TO_SHOW = 600
IMAGE_HEIGHT_TO_SHOW = 600

INPUT_NUM_TRYS = 2
POPPLER_PATH = "C:\\poppler-20.09.0\\bin"

original_image_array_show = []
images_numpy_array = []
images_numpy_array_show = []
imageTK_list = []
images_path_list = []
original_image_array = []
LABEL = ":תיוג"
writerID = ""
points = []
images_path_list = []
images = []
txt_file = []
delete_files = []

global root

def reset_global_parameters():
    global folder_selected, markTextArea, markTextArea, images, original_image_array_show, images_numpy_array
    global images_numpy_array_show, imageTK_list, original_image_array
    global  scannedInsertDocuments, delete_files, txtFiles, points,images_path_list, status_program
    folder_selected = ""
    markTextArea = False
    status_program = None
    scannedInsertDocuments = None
    delete_files = []
    txtFiles = []
    points = []
    images =[]
    images_path_list = []
    original_image_array_show = []
    images_numpy_array = []
    images_numpy_array_show = []
    imageTK_list = []
    original_image_array = []


def popup_message(message, type):
    if type.lower() == "information":
        response = messagebox.showinfo("information", message)
    elif type.lower() == "error":
        response = messagebox.showerror("ERROR", message)
    elif type.lower() == "warning":
        response = messagebox.showwarning("WARNING", message)















def userSetLabel(line_images_array):
    global my_image_check_data, good_Image, bad_Image, image_list, status, root_checkData
    root_setLabel = Toplevel()
    root_setLabel.title("Set labels for new handwriting lines")

    for image_array in line_images_array:
        width, height = calculate_width_height(image_array, IMAGE_WIDTH_TO_SHOW, IMAGE_HEIGHT_TO_SHOW)
        image_array = cv.resize(image_array, (width, height))
        imageTK = ImageTk.PhotoImage(Image.fromarray(image_array))
        image_list.append(imageTK)

    status = Label(root_checkData, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN)
    label_image_name = DataManager.getLabelFromDatabase(path_list[0])
    if label_image_name == -1:
        popup_message("The text file of image - " + os.path.basename(path_list[0]) + " not found", maessage_type(2))
        label_image_name = "ERROR"
    label_title = Label(root_checkData, text=LABEL, anchor="e")
    my_label_check_data = Label(root_checkData, text=label_image_name, anchor="e")

    label_title.grid(row=2, column=0, columnspan=3, sticky="ew", pady=5)
    my_label_check_data.grid(row=3, column=0, columnspan=3, sticky="ew")

    my_image_check_data = Label(root_checkData, image=image_list[0], width=IMAGE_WIDTH_TO_SHOW)
    my_image_check_data.grid(row=0, column=0, columnspan=3)

    button_exit = Button(root_checkData, text="Exit", padx=30, pady=20,
                         command=lambda: exit_check_data(root_checkData, bad_Image))

    button_eccept = Button(root_checkData, text="OK", padx=70, pady=20, command=lambda: foward(True, 1, path_list),
                           fg="black", bg="green")
    button_remove = Button(root_checkData, text="Error", padx=70, pady=20,
                           command=lambda: foward(False, 1, path_list), fg="black", bg="red")

    button_exit.grid(row=1, column=0)
    button_eccept.grid(row=1, column=1)
    button_remove.grid(row=1, column=2)
    status.grid(row=4, column=0, columnspan=3)
    root_checkData.mainloop()
    return bad_Image



def foward(sign, image_number, path_list):
    global my_image_check_data, button_eccept, button_remove, status, good_Image, bad_Image, image_list, root_checkData
    if sign:
        good_Image.append(path_list[image_number - 1])
    else:
        bad_Image.append(path_list[image_number - 1])
    my_image_check_data.grid_forget()
    my_image_check_data = Label(root_checkData, image=image_list[image_number], width=IMAGE_WIDTH_TO_SHOW)

    if image_number == len(image_list) - 1:
        button_eccept = Button(root_checkData, text="OK", padx=70, pady=20,
                               command=lambda: eccept(image_number, path_list), fg="black",
                               bg="green")
        button_remove = Button(root_checkData, text="Error", padx=70, pady=20,
                               command=lambda: remove(image_number, path_list),
                               fg="black", bg="red")
    else:
        button_eccept = Button(root_checkData, text="OK", padx=70, pady=20,
                               command=lambda: foward(True, image_number + 1, path_list),
                               fg="black", bg="green")
        button_remove = Button(root_checkData, text="Error", padx=70, pady=20,
                               command=lambda: foward(False, image_number + 1, path_list), fg="black", bg="red")
    status = Label(root_checkData, text="Image " + str(image_number + 1) + " of " + str(len(image_list)), bd=1,
                   relief=SUNKEN)
    label_image_name = DataManager.getLabelFromDatabase(path_list[image_number])
    if label_image_name == -1:
        popup_message("The text file of image - " + os.path.basename(image_list[image_number]) + " not found",
                      maessage_type(2))
        label_image_name = "ERROR"
    label_title = Label(root_checkData, text=LABEL, anchor="e")
    my_label_check_data = Label(root_checkData, text=label_image_name, anchor="e")

    label_title.grid(row=2, column=0, columnspan=3, sticky="ew", pady=5)
    my_label_check_data.grid(row=3, column=0, columnspan=3, sticky="ew")
    status.grid(row=4, column=0, columnspan=3)
    my_image_check_data.grid(row=0, column=0, columnspan=3)
    button_eccept.grid(row=1, column=1)
    button_remove.grid(row=1, column=2)

def exit_program(root):
    root.destroy()

def exit_check_data(root, bad_Image):
    global deleteFiles
    root.destroy()
    DataManager.delete_from_database(bad_Image)
    if bad_Image != []:
        popup_message("Deleted images", maessage_type(0))
    else:
        popup_message("THANK YOU :)", maessage_type(0))
    deleteFiles()







def CheckImage(file):
    valid_images = [".jpg", ".gif", ".png", ".tif", ".tiff"]
    ext = os.path.splitext(file)[1]
    if ext.lower() not in valid_images:
        return False
    else:
        return True

def CheckPDF(file):
    ext = os.path.splitext(file)[1]
    if ext.lower() =='.pdf':
        return True
    else:
        return False

# The Image of the training will be extract to same path where it save
def ExtractImagesFromPDF(file, files):
    global delete_files, writerID
    order = HandwrittenDoc.check_PDF_name(file)
    images = convert_from_path(file, fmt="jpeg", poppler_path =POPPLER_PATH)
    outputpath, namefile = os.path.split(file)
    i = 0
    for image in images:
        # image = Image.open(im)
        new_path_image = os.path.join(outputpath, writerID +"_"+ str(order[i]) + ".tif")
        j=0
        while (new_path_image in files):
            new_path_image = os.path.join(outputpath, writerID + "_"+str(j)+"_" + str(order[i]) + ".tif")
            j += 1
        i += 1
        image.save(new_path_image, 'TIFF')
        files.append(new_path_image)
        delete_files.append(new_path_image)
    return files

# the func save all the paths of the images and text files(optional)
# input: path of a folder,  scanned = false if want to find also text files
# output: list of all the images ans text files
def Extract_files_from_folder(folder):
    imagesInFolder = []
    txtFiles = []
    files = os.listdir(folder)
    flag = 0
    for file in files:
        if (CheckImage(file) == False) :
            if (CheckPDF(file) == True ):
                files = files + ExtractImagesFromPDF(os.path.join(folder,file), files)
            continue
        else:
            if not HandwrittenDoc.Check_image_name(file):
                namefile = os.path.basename(file)
                popup_message("WRONG INPUT IMAGE NAME - "+namefile,  maessage_type(1))
                continue
        imagesInFolder.append(os.path.join(folder, file))

    return imagesInFolder, txtFiles


def deleteFiles():
    global delete_files
    for file in delete_files:
        os.remove(file)
    delete_files = []

def openFolder():
    global frame_scanned_label, folder_selected, frame, root, mark_Button, run_Button, frameMarkRun
    frameMarkRun = Frame(root)
    frameMarkRun.grid(row=5, column=0, columnspan=2)

    root.withdraw()
    folder_selected = filedialog.askdirectory()
    root.deiconify()
    mylabel_folder = Label(frame_scanned_label, text=folder_selected)
    mylabel_folder.grid(row=2, column=0, columnspan = 2)
    mark_Button = Button(frameMarkRun, text="Mark the text", command=Popup_Mark_the_text, bg="hot pink").grid(row=0, column=0, columnspan = 2)
    run_Button = Button(frameMarkRun, text = "RUN", command = run_program, bg="turquoise").grid(row=1, column=0, columnspan = 2)


def checkID(writerID):
    if writerID == "":
        return False
    if len(writerID)>9 or ord(writerID[0]) < 49 or ord(writerID[0]) >= 60:
        return False
    return True

def enterID():
    global e, writerID
    writerID =  e.get()
    if not checkID(writerID):
        popup_message("You enter wrong ID, Try Again", maessage_type(2))
        return -1
    #popup_message("succeeded", maessage_type(0))
    return 1


def clicked_Radiobutton(value):
    global myButton, frame, frame_scanned_label, folder_selected
    global folder_selected, scannedInsertDocuments, frameExtract, frameMarkRun, e
    images = []
    frameMarkRun.destroy()
    frameExtract.destroy()
    frame_text.destroy()

    frame_scanned_label.destroy()
    frame_scanned_label = Frame(frame)
    frame_scanned_label.grid(row=4, column=0, columnspan=2)

    folder_selected = ""

    if value ==insertDocuments("Scanned"):

        scannedInsertDocuments = True
        myButton = Button(frame_scanned_label, text="Select Folder with scanned paged (PDF \ Image formats)", padx = 10, pady = 20,  command=openFolder)

    elif value ==insertDocuments("Labeled"):
        scannedInsertDocuments = False
        myButton = Button(frame_scanned_label, text="Open Image of your handwrite ", padx=10, pady=20, command=get_image)

    e = Entry(frame_scanned_label, width=50, borderwidth=5)
    enterButton = Button(frame_scanned_label, text="Enter writer ID", command=enterID, fg="black")
    myButton.grid(row=1,column = 0, columnspan=2)

    enterButton.grid(row=3,column = 0)
    e.grid(row=3, column=1)
    mainloop()

def Popup_Mark_the_text():
    global markTextArea
    response = messagebox.askyesno("Mark the text", "Do you wont to select the area of the text on the documents?")
    markTextArea = response

def chooseScannedOrLabeled():
    global mylabel_radio, clicked, frame, frame_scanned_label
    frame_scanned_label = Frame(frame)
    frame_scanned_label.grid(row=4, column =0, columnspan = 2)
    r = IntVar()
    r.set("1")
    myLabel = Label(frame, text="Colecting data for training tesseract")
    Radiobutton1 = Radiobutton(frame, text = "Scanned handwrite images", variable = r, value = 0, command = lambda:clicked_Radiobutton(r.get()))
    Radiobutton2 = Radiobutton(frame, text = "Create your labeled handwrite data", variable = r, value = 1, command = lambda:clicked_Radiobutton(r.get()))

    myLabel.grid(row=0, column=0, columnspan =2)
    Radiobutton1.grid(row=3, column=0)
    Radiobutton2.grid(row=3, column=1)
    frame.mainloop()

# show the image that was selecr=ted for "extract text" process
def show_image():
    global frameExtract, flag_show, canvas_image, images_path_list, imageTK_list, show_image_butten, hide_image_butten
    imageTK = imageTK_list[0]
    canvas_image = Canvas(frameExtract, width = imageTK.width(), height = imageTK.height())
    canvas_image.grid(row=1, column=0, columnspan=2)

    canvas_image.create_image((0,0) , image = imageTK, anchor="nw")
    flag_show = 0

    show_image_butten = Button(frameExtract, text="show image", state=DISABLED).grid(row=0, column=0)
    hide_image_butten = Button(frameExtract, text="hide image", command=hide_image).grid(row=0, column=1)

def hide_image():
    global frameExtract, canvas_image, show_image_butten, hide_image_butten
    canvas_image.delete('all')
    canvas_image.grid_forget()
    show_image_butten = Button(frameExtract, text="show image", command=show_image).grid(row=0, column=0)
    hide_image_butten = Button(frameExtract, text="hide image", state=DISABLED).grid(row=0, column=1)


def slide_threshold(image_array, root):
    global imageTK_, my_image_label, choosenImage, horizontal, btn_dilation, btn_opening, btn_closing, choosenImage_originsize

    _, th = cv.threshold(image_array, horizontal.get(), 255, cv.THRESH_BINARY)
    _, choosenImage_originsize = cv.threshold(choosenImage_originsize, horizontal.get(), 255, cv.THRESH_BINARY)
    choosenImage = th.copy()

    image_array = th.copy()
    width, height = calculate_width_height(image_array, IMAGE_WIDTH_TO_SHOW, IMAGE_HEIGHT_TO_SHOW)
    image_array = cv.resize(image_array, (width, height))

    image_fromarray = Image.fromarray(image_array)
    imageTK_ = ImageTk.PhotoImage(image_fromarray)
    my_image_label = Label(root, image=imageTK_)
    my_image_label.grid(row=1, column=0, rowspan = 5)

    btn_dilation = Button(root, text = "dilation", command = lambda: dilation(root)).grid(row = 2, column = 3)
    btn_opening = Button(root, text = "opening", command = lambda: opening(root)).grid(row = 2, column = 2)
    btn_closing = Button(root, text = "closing", command = lambda: closing(root)).grid(row = 2, column = 1)

def get_original(root):
    global my_image_label, original, imageTK_, choosenImage, choosenImage_originsize, images_numpy_array, top_edit
    choosenImage_originsize = images_numpy_array[0].copy()
    choosenImage = original.copy()
    image_array = original.copy()
    width, height = calculate_width_height(image_array, IMAGE_WIDTH_TO_SHOW, IMAGE_HEIGHT_TO_SHOW)
    image_array = cv.resize(image_array, (width, height))

    image_fromarray = Image.fromarray(image_array)
    imageTK_ = ImageTk.PhotoImage(image_fromarray)

    my_image_label = Label(root, image=imageTK_)
    my_image_label.grid(row=1, column=0, rowspan = 5)

def save_edit_image():
    global choosenImage, top_edit, isTrain, root, scannedInsertDocuments
    global images_numpy_array_show, images_numpy_array, imageTK_list, choosenImage_originsize
    print (choosenImage)
    images_numpy_array_show[0] = choosenImage
    images_numpy_array[0] = choosenImage_originsize
    imageTK_list[0] = ImageTk.PhotoImage(Image.fromarray(images_numpy_array_show[0]))
    # cv.imshow("images_numpy_array_show", images_numpy_array_show[0])
    # cv.imshow("images_numpy_array", images_numpy_array[0])
    # cv.waitKey()
    images.append(ImageProcessing.ImageProcessing(images_numpy_array[0], imagePath=images_path_list[0]))

    print("isTrain"+str(isTrain))
    print("scannedInsertDocuments "+str(scannedInsertDocuments))
    controller = Controller.Controller(isTrain, images, root, isScanned = scannedInsertDocuments)
    result = controller.main()
    top_edit.destroy()
    showResults(root, result)


def dilation(root):
    global my_image_label, original, imageTK_, choosenImage, btn_dilation, choosenImage_originsize, top_edit
    image_array = choosenImage.copy()
    kernal = np.ones((2, 2), np.uint8)
    dilation = cv.dilate(image_array, kernal, iterations=3)
    choosenImage_originsize = cv.dilate(choosenImage_originsize, kernal, iterations=3)

    choosenImage = dilation.copy()
    width, height = calculate_width_height(image_array, IMAGE_WIDTH_TO_SHOW, IMAGE_HEIGHT_TO_SHOW)
    image_array = cv.resize(image_array, (width, height))
    image_fromarray = Image.fromarray(image_array)
    imageTK_ = ImageTk.PhotoImage(image_fromarray)
    my_image_label = Label(root, image=imageTK_)
    my_image_label.grid(row=1, column=0, rowspan = 5)
    btn_dilation = Button(root, text = "dilation", state = DISABLED).grid(row = 2, column = 3)

def opening(root):
    global my_image_label, original, imageTK_, choosenImage, btn_dilation, btn_opening, choosenImage_originsize, top_edit
    image_array = choosenImage.copy()
    kernal = np.ones((2, 2), np.uint8)
    opening = cv.morphologyEx(image_array, cv.MORPH_OPEN, kernal)
    choosenImage_originsize = cv.morphologyEx(choosenImage_originsize, cv.MORPH_OPEN, kernal)

    choosenImage = opening.copy()
    width, height = calculate_width_height(image_array, IMAGE_WIDTH_TO_SHOW, IMAGE_HEIGHT_TO_SHOW)
    image_array = cv.resize(image_array, (width, height))
    image_fromarray = Image.fromarray(image_array)
    imageTK_ = ImageTk.PhotoImage(image_fromarray)
    my_image_label = Label(root, image=imageTK_)
    my_image_label.grid(row=1, column=0, rowspan = 5)
    btn_opening = Button(root, text = "opening", state = DISABLED).grid(row = 2, column = 2)

def closing(root):
    global my_image_label, original, imageTK_, choosenImage, btn_closing, choosenImage_originsize, top_edit
    image_array = choosenImage.copy()
    kernal = np.ones((2, 2), np.uint8)
    closing = cv.morphologyEx(image_array, cv.MORPH_CLOSE, kernal)
    choosenImage_originsize = cv.morphologyEx(choosenImage_originsize, cv.MORPH_CLOSE, kernal)
    choosenImage = closing.copy()
    width, height = calculate_width_height(image_array, IMAGE_WIDTH_TO_SHOW, IMAGE_HEIGHT_TO_SHOW)
    image_array = cv.resize(image_array, (width, height))
    image_fromarray = Image.fromarray(image_array)
    imageTK_ = ImageTk.PhotoImage(image_fromarray)
    my_image_label = Label(root, image=imageTK_)
    my_image_label.grid(row=1, column=0, rowspan = 5)
    btn_closing = Button(root, text = "closing", state = DISABLED).grid(row = 2, column = 1)

def userChooseTresholds(image_array, root):
    global horizontal, choosenImage, choosenImage_originsize, original, my_image_label, imageTK_, get_original_button
    global btn_dilation, btn_opening, btn_closing, top_edit, images_numpy_array

    horizontal = Scale(root, from_ =  0, to =  255, orient = HORIZONTAL)
    horizontal.grid(row = 1, column = 2)
    my_label = Label(root, text = "choose value for\n THRESH_BINARY: ")
    my_label.grid(row = 1, column = 1)

    #image_array = cv.imread(image_path, 0)
    choosenImage_originsize = images_numpy_array[0].copy()

    original = image_array.copy()

    width, height = calculate_width_height(image_array, IMAGE_WIDTH_TO_SHOW, IMAGE_HEIGHT_TO_SHOW)
    image_array = cv.resize(image_array, (width, height))
    choosenImage = image_array.copy()

    root.geometry(str(width + 300) + "x" + str(height + 100))

    image_fromarray = Image.fromarray(image_array)
    imageTK_ = ImageTk.PhotoImage(image_fromarray)
    my_title = Label(root, text = "Find the best variation of your image to extracting text", font=("Ariel", 16))
    my_title.grid(row = 0, column = 0, columnspan = 5)

    my_image_label = Label(root, image=imageTK_)
    my_image_label.grid(row=1, column=0, rowspan = 5)

    btn_THRESH_BINARY = Button(root, text = "click", command = lambda: slide_threshold(image_array, root)).grid(row = 1, column = 3)

    btn_dilation = Button(root, text = "dilation", state = DISABLED).grid(row = 2, column = 3)
    btn_opening = Button(root, text = "opening", state = DISABLED).grid(row = 2, column = 2)
    btn_closing = Button(root, text = "closing", state = DISABLED).grid(row = 2, column = 1)
    get_original_button = Button(root, text = "click to original", command = lambda: get_original(root), width = 25).grid(row = 5, column = 1, columnspan = 3)
    save_image_button = Button(root, text="Click here to run program on this image", command=save_edit_image).grid(row=8, column=0, columnspan = 4)
    root.mainloop()

def EditImage():
    global images_numpy_array_show, images_numpy_array
    global choosenImage, original, root, top_edit
    top_edit = Toplevel()
    top_edit.title("Edit you image")
    userChooseTresholds(images_numpy_array[0].copy(), top_edit)


def get_image():
    global root, frame, clicked, options, flag_show, frameExtract, mark_Button, frameMarkRun, imageTK_list, images_path_list
    global original_image_array, images_numpy_array, images_numpy_array_show, show_image_button, hide_image_button, original_image_array_show
    images_path_list = []
    imageTK_list = []
    images_numpy_array_show = []
    images_numpy_array =[]
    frameExtract.destroy()
    frameExtract = Frame(frame)
    frameMarkRun = Frame(root)
    frameMarkRun.grid(row=6, column=0, columnspan=2)

    frameExtract.grid(row=5, column=0, columnspan=2)
    flag_show = 1
    root.filename = filedialog.askopenfilename(title="select a file", filetype=(("ALL FILES", "*.*"),("JPEG", "*.jpg"),("PNG", "*.png"), ("TIF", "*.tif")))
    images_path_list.append(root.filename)

    image_array = cv.imread(images_path_list[0], 0)
    original_image_array.append(image_array.copy())
    images_numpy_array.append(image_array.copy())
    width, height = calculate_width_height(image_array, IMAGE_WIDTH_TO_SHOW, IMAGE_HEIGHT_TO_SHOW)
    image_array = cv.resize(image_array, (width, height))
    images_numpy_array_show.append(image_array)
    original_image_array_show = images_numpy_array_show.copy()
    imageTK_list.append(ImageTk.PhotoImage(Image.fromarray(image_array)))

    show_image_button = Button(frameExtract, text="show image", command=show_image).grid(row=0, column=0)
    hide_image_button = Button(frameExtract, text="hide image", state=DISABLED).grid(row=0, column=1)
    #edit_image_button = Button(frameExtract, text="Edit image", command=EditImage).grid(row=0, column=2, sticky=W + E)

    mark_Button = Button(frameMarkRun, text="Mark the text", command=Popup_Mark_the_text, bg="hot pink").grid(row=0, column=0, columnspan = 2)
    run_Button = Button(frameMarkRun, text="RUN", command=run_program, bg="turquoise").grid(row=1, column=0, columnspan = 2)

def Select_train_test(var):
    global myLabel, clicked, frame, options, root, status_program, image_label, frameExtract, frameMarkRun, frame_text
    global insert_image_button
    reset_global_parameters()
    frame.destroy()
    frameMarkRun.destroy()
    frameExtract.destroy()
    frame_text.destroy()
    value = clicked.get()
    frame = Frame(root)
    frame.grid(row=3, column=0, columnspan=2)

    #is Train - collect Data
    if value == Status_program(0):
        status_program = Status_program(0)
        myLabel = Label(frame, text="Collecting data for training tesseract").grid(row=0, column =0, columnspan = 2)

        drop = OptionMenu(root, clicked, *options, command=Select_train_test)
        drop.grid(row=1, column=0, columnspan = 2)
        chooseScannedOrLabeled()

    if value == Status_program(1):
        status_program = Status_program(1)
        myLabel = Label(frame, text="Run tesseract on the lateset training machine").grid(row=0,  column =0, columnspan = 2)
        drop = OptionMenu(root, clicked, *options, command=Select_train_test)
        drop.grid(row=1, column=0, columnspan = 2)
        insert_image_button = Button(frame, text="Open image", command=get_image).grid(row=2, column=0, columnspan = 2)
        # showImageAndExtractedText()
    frame.mainloop()

def eccept(image_number, path_list):
    global my_image_check_data, button_eccept, button_remove, good_Image, bad_Image, image_list, root_window
    global status, good_Image, image_list, my_label_check_data
    good_Image.append(path_list[image_number])

    status.grid_forget()
    my_image_check_data.grid_forget()
    my_image_check_data = Label(root_checkData, image=image_list[image_number+1], width  = IMAGE_WIDTH_TO_SHOW)
    button_eccept = Button(root_checkData, text="OK", padx=70, pady=20, state=DISABLED, fg="black",
                           bg="green")
    button_remove = Button(root_checkData, text="Error", padx=70, pady=20, state=DISABLED, fg="black",
                           bg="red")

    status = Label(root_checkData, text="Image " + str(image_number + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN)
    label_image_name = DataManager.getLabelFromDatabase(path_list[image_number])
    if label_image_name == -1:
        popup_message("The text file of image - "+ os.path.basename(image_list[image_number]) +" not found", maessage_type(2))
        label_image_name = "ERROR"
    label_title = Label(root_checkData, text = LABEL, anchor = "e")
    my_label_check_data = Label(root_checkData, text = label_image_name, anchor = "e")

    label_title.grid(row=2, column=0, columnspan=3, sticky = "ew", pady=5)
    my_label_check_data.grid(row=3, column=0, columnspan=3, sticky = "ew")
    status.grid(row=4, column=0, columnspan=3)

    my_image_check_data.grid(row=0, column=0, columnspan=3)
    button_eccept.grid(row=1, column=1)
    button_remove.grid(row=1, column=2)

def remove(image_number, path_list):
    global my_image_check_data, button_eccept, button_remove, status, good_Image, bad_Image, image_list, root_checkData
    bad_Image.append(path_list[image_number])
    status.grid_forget()
    my_image_check_data.grid_forget()
    my_image_check_data = Label(root_checkData, image=image_list[image_number+1], width  = IMAGE_WIDTH_TO_SHOW)
    button_eccept = Button(root_checkData, text="OK", padx=70, pady=20, state=DISABLED, fg="black",
                           bg="green")
    button_remove = Button(root_checkData, text="Error", padx=70, pady=20, state=DISABLED, fg="black",
                           bg="red")
    status = Label(root_checkData, text="Image " + str(image_number + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN)
    label_image_name = DataManager.getLabelFromDatabase(path_list[image_number])
    if label_image_name == -1:
        popup_message("The text file of image - "+ os.path.basename(image_list[image_number]) +" not found", maessage_type(2))
        label_image_name = "ERROR"
    label_title = Label(root_checkData, text = LABEL, anchor = "e")
    my_label_check_data = Label(root_checkData, text = label_image_name, anchor = "e")

    label_title.grid(row=2, column=0, columnspan=3, sticky = "ew", pady=5)
    my_label_check_data.grid(row=3, column=0, columnspan=3, sticky = "ew")
    status.grid(row=4, column=0, columnspan=3)
    my_image_check_data.grid(row=0, column=0, columnspan=3)
    button_eccept.grid(row=1, column=1)
    button_remove.grid(row=1, column=2)

def foward(sign, image_number, path_list):
    global my_image_check_data, button_eccept, button_remove, status, good_Image, bad_Image, image_list, root_checkData
    if sign:
        good_Image.append(path_list[image_number - 1])
    else:
        bad_Image.append(path_list[image_number - 1])
    my_image_check_data.grid_forget()
    my_image_check_data = Label(root_checkData, image=image_list[image_number], width  = IMAGE_WIDTH_TO_SHOW)

    if image_number == len(image_list) - 1:
        button_eccept = Button(root_checkData, text="OK", padx=70, pady=20, command=lambda: eccept(image_number, path_list), fg="black",
                               bg="green")
        button_remove = Button(root_checkData, text="Error", padx=70, pady=20, command=lambda: remove(image_number, path_list),
                               fg="black", bg="red")
    else:
        button_eccept = Button(root_checkData, text="OK", padx=70, pady=20, command=lambda: foward(True, image_number + 1, path_list),
                               fg="black", bg="green")
        button_remove = Button(root_checkData, text="Error", padx=70, pady=20,
                               command=lambda: foward(False, image_number + 1, path_list), fg="black", bg="red")
    status = Label(root_checkData, text="Image " + str(image_number + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN)
    label_image_name = DataManager.getLabelFromDatabase(path_list[image_number])
    if label_image_name == -1:
        popup_message("The text file of image - "+ os.path.basename(image_list[image_number]) +" not found", maessage_type(2))
        label_image_name = "ERROR"
    label_title = Label(root_checkData, text = LABEL, anchor = "e")
    my_label_check_data = Label(root_checkData, text = label_image_name, anchor = "e")

    label_title.grid(row=2, column=0, columnspan=3, sticky = "ew", pady=5)
    my_label_check_data.grid(row=3, column=0, columnspan=3, sticky = "ew")
    status.grid(row=4, column=0, columnspan=3)
    my_image_check_data.grid(row=0, column=0, columnspan=3)
    button_eccept.grid(row=1, column=1)
    button_remove.grid(row=1, column=2)


def exit_program(root):
    root.destroy()

def exit_check_data(root, bad_Image):
    global deleteFiles
    root.destroy()
    DataManager.delete_from_database(bad_Image)
    if bad_Image!=[]:
        popup_message("Deleted images", maessage_type(0))
    else:
        popup_message("THANK YOU :)", maessage_type(0))
    deleteFiles()

def checkData(path_list, top):
    global my_image_check_data, good_Image, bad_Image, image_list, status, root_checkData
    good_Image = []
    bad_Image = []
    image_list = []
    root_checkData = top
    for image_path in path_list:
        image_array = cv.imread(image_path, 0)
        width, height = calculate_width_height(image_array, IMAGE_WIDTH_TO_SHOW, IMAGE_HEIGHT_TO_SHOW)
        image_array = cv.resize(image_array, (width, height))
        imageTK = ImageTk.PhotoImage(Image.fromarray(image_array))

        image_list.append(imageTK)

    status = Label(root_checkData, text = "Image 1 of " + str(len(image_list)), bd =1, relief = SUNKEN)
    label_image_name = DataManager.getLabelFromDatabase(path_list[0])
    if label_image_name == -1:
        popup_message("The text file of image - "+ os.path.basename(path_list[0]) +" not found", maessage_type(2))
        label_image_name = "ERROR"
    label_title = Label(root_checkData, text = LABEL, anchor = "e")
    my_label_check_data = Label(root_checkData, text = label_image_name, anchor = "e")

    label_title.grid(row=2, column=0, columnspan=3, sticky = "ew", pady=5)
    my_label_check_data.grid(row=3, column=0, columnspan=3, sticky = "ew")

    my_image_check_data = Label(root_checkData, image = image_list[0], width  = IMAGE_WIDTH_TO_SHOW)
    my_image_check_data.grid(row = 0, column = 0, columnspan = 3)

    button_exit = Button(root_checkData, text = "Exit",padx = 30, pady = 20, command = lambda: exit_check_data(root_checkData, bad_Image))

    button_eccept = Button(root_checkData, text="OK", padx=70, pady=20, command=lambda: foward(True, 1, path_list), fg="black", bg="green")
    button_remove = Button(root_checkData, text="Error", padx=70, pady=20, command=lambda: foward(False, 1, path_list), fg="black", bg="red")

    button_exit.grid(row = 1, column = 0)
    button_eccept.grid(row = 1, column = 1)
    button_remove.grid(row = 1, column = 2)
    status.grid(row=4, column = 0 , columnspan = 3)
    root_checkData.mainloop()
    return bad_Image

def new_window_check_database(root):
    path_list = DataManager.list_image_path_database()
    top = Toplevel()
    top.title("check database")
    checkData(path_list, top)


def covert_points_from_resize_to_original(points, resizeImage, originalImage):
    width_resizeImage = resizeImage.shape[1]
    height_resizeImage = resizeImage.shape[0]

    width_originalImage = originalImage.shape[1]
    height_originalImage = originalImage.shape[0]

    new_points = []
    if width_resizeImage == width_originalImage:
        return points
    coeff = width_originalImage / width_resizeImage
    for point in points:
        new_points.append((math.floor(point[0]*(width_originalImage / width_resizeImage)), math.floor(point[1] *coeff)))
    return new_points

def click_CutImage(num_image) :
    global points, file, top2, w, num_image_to_cut, imageTK_list, original_image_array_show, img_toCut, cv_array
    top2 = Toplevel()
    top2.title("Cut image window")
    points = []
    num_image_to_cut = num_image
    w = Canvas(top2, width=IMAGE_WIDTH_TO_SHOW, height=IMAGE_HEIGHT_TO_SHOW)
    cv_array = original_image_array_show[num_image_to_cut].copy()
    img_toCut = ImageTk.PhotoImage(Image.fromarray(cv_array))
    w.create_image(0, 0, image=img_toCut, anchor="nw")
    w.grid(row=0)
    top2.bind("<Button 1>", CutImage)

def CutImage(eventorigin):
    global x, y, points, top2, w, images_path_list, images_numpy_array_show, num_image_to_cut, root_window, img_toCut, cv_array
    global original_image_array, original_image_array_show, my_image
    while(len(points)<4):
        x = eventorigin.x
        y = eventorigin.y
        cv_array = cv.circle(cv_array, (x, y), 3, 0, -1)
        points.append((x, y))
        if len(points) >= 2:
            cv_array = cv.line(cv_array, points[-1], points[-2], 50, 3)

        img_toCut = ImageTk.PhotoImage(Image.fromarray(cv_array))
        w.create_image(0, 0, image=img_toCut, anchor="nw")
        top2.bind("<Button 1>", CutImage)
        top2.mainloop()

    top2.destroy()

    fixed_points = covert_points_from_resize_to_original(points, resizeImage = original_image_array_show[num_image_to_cut], originalImage = original_image_array[num_image_to_cut])
    print(fixed_points)
    print(points)

    images_numpy_array_show[num_image_to_cut] = ImageProcessing.WrapImage(original_image_array_show[num_image_to_cut], np.array(points[0:4]))
    images_numpy_array[num_image_to_cut] = ImageProcessing.WrapImage(original_image_array[num_image_to_cut] , np.array(fixed_points[0:4]))
    imageTK_list[num_image_to_cut] = ImageTk.PhotoImage(Image.fromarray(images_numpy_array_show[num_image_to_cut]))

    status = Label(root_window, text = "Image "+str(num_image_to_cut+1)+" of " + str(len(imageTK_list)), bd =1, relief = SUNKEN)
    my_image.grid_forget()
    my_image = Label(root_window, image = imageTK_list[num_image_to_cut])
    my_image.grid(row = 0, column = 1, columnspan = 3)
    button_exit = Button(root_window, text = "Exit",padx = 70, pady = 20, command = exit_wrap)
    button_wrap = Button(root_window, text = "try again Cut Image",padx = 70, pady = 20, command = lambda: click_CutImage(num_image_to_cut))
    if num_image_to_cut == len(imageTK_list)-1:
        button_next = Button(root_window, text=">>", padx=70, pady=20, state=DISABLED, fg="black")
    else:
        button_next = Button(root_window, text=">>", padx=70, pady=20, command=lambda: next(num_image_to_cut + 1),
                             fg="black")

    if num_image_to_cut ==0:
        button_previous = Button(root_window, text="<<", padx=70, pady=20, state = DISABLED, fg="black")
    else:
        button_previous = Button(root_window, text="<<", padx=70, pady=20, command=lambda: back(num_image_to_cut - 1),
                                 fg="black")

    button_exit.grid(row = 1, column = 0)
    button_wrap.grid(row = 1, column = 1,  columnspan = 2)
    button_next.grid(row = 0, column =4)
    button_previous.grid(row = 0, column = 0)
    status.grid(row=3, column = 0 , columnspan = 3)
    root_window.mainloop()

def next( image_number):
    global my_image, button_next, button_previous, status, good_Image, bad_Image, imageTK_list, images_path_list, root_window, button_wrap

    my_image.grid_forget()

    my_image = Label(root_window, image=imageTK_list[image_number])

    if image_number == len(images_path_list) - 1:
        button_next = Button(root_window, text=">>", padx=70, pady=20, state=DISABLED, fg="black")
    else:
        button_next = Button(root_window, text=">>", padx=70, pady=20, command=lambda: next(image_number + 1),fg="black")

    button_previous = Button(root_window, text="<<", padx=70, pady=20,command=lambda: back(image_number -1), fg="black")

    status = Label(root_window, text="Image " + str(image_number+1) + " of " + str(len(imageTK_list)), bd=1, relief=SUNKEN)
    button_wrap = Button(root_window, text="Cut Image", padx=70, pady=20, command=lambda: click_CutImage(image_number))

    button_wrap.grid(row=1, column=1, columnspan=2)
    my_image.grid(row=0, column=1, columnspan=3)
    button_next.grid(row = 0, column =4)
    button_previous.grid(row=0, column=0)
    status.grid(row=3, column=0, columnspan=3)


def back( image_number):
    global my_image, button_next, button_previous, status, good_Image, bad_Image, imageTK_list, images_path_list, root_window
    my_image.grid_forget()

    my_image = Label(root_window, image=imageTK_list[image_number])
    button_next = Button(root_window, text=">>", padx=70, pady=20, command=lambda: next(image_number + 1), fg="black")

    if image_number == 0:
        button_previous = Button(root_window, text="<<", padx=70, pady=20,state = DISABLED, fg="black")
    else:
        button_previous = Button(root_window, text="<<", padx=70, pady=20, command=lambda: back(image_number - 1), fg="black")

    button_wrap = Button(root_window, text="Cut Image", padx=70, pady=20, command=lambda: click_CutImage(image_number))
    status = Label(root_window, text="Image " + str(image_number +1) + " of " + str(len(imageTK_list)), bd=1, relief=SUNKEN)

    button_wrap.grid(row=1, column=1, columnspan=2)
    my_image.grid(row=0, column=1, columnspan=3)
    button_next.grid(row = 0, column =4)
    button_previous.grid(row=0, column = 0)
    status.grid(row=3, column=0, columnspan=3)

def exit_wrap():
    global root_window
    root_window.destroy()
    run_program(finishWrop = True)

def wrap_data():
    global my_image, imageTK_list, status, root_window, images_numpy_array_show, root_window
    global original_image_array
    root_window = Toplevel()
    root_window.title("Cropp the image")

    status = Label(root_window, text = "Image 1 of " + str(len(imageTK_list)), bd =1, relief = SUNKEN)

    my_image = Label(root_window, image = imageTK_list[0])
    my_image.grid(row = 0, column = 1, columnspan = 3)

    button_exit = Button(root_window, text = "Exit",padx = 70, pady = 20, command = exit_wrap)
    button_wrap = Button(root_window, text = "Cut Image",padx = 70, pady = 20, command = lambda: click_CutImage(0))
    button_next = Button(root_window, text=">>", padx=70, pady=20, command=lambda: next(1), fg="black")
    button_previous = Button(root_window, text="<<", padx=70, pady=20, state = DISABLED, fg="black")

    button_exit.grid(row = 1, column = 0)
    button_wrap.grid(row = 1, column = 1,  columnspan = 2)
    button_next.grid(row = 0, column =4)
    button_previous.grid(row = 0, column = 0)
    status.grid(row=3, column = 0 , columnspan = 3)
    root.mainloop()


def calculate_width_height(image_array, max_width_to_show, max_height_to_show):
    width_original = image_array.shape[1]
    height_original = image_array.shape[0]
    if width_original < max_width_to_show and height_original  < max_height_to_show:
        return width_original, height_original

    if width_original > height_original:
        new_width = max_width_to_show
        new_height = math.floor(height_original * (max_width_to_show / width_original))
    else:
        new_height = max_height_to_show
        new_width = math.floor(width_original * (max_height_to_show / height_original))

    return new_width, new_height

def extractResult(result):
    # root.withdraw()
    # folder_to_save = filedialog.askdirectory()
    # root.deiconify()
    # baseNameImage = os.path.basename(images[0].imagePath)
    # nameImage = os.path.splitext(baseNameImage)[0]
    # f = open(os.path.join(folder_to_save,  nameImage+ ".txt"), "w+", encoding="utf-8")
    # f.write(result)
    # f.close()
    # popup_message("Secceeded, hope to see you again :)", maessage_type(0))
    root.withdraw()
    file_to_save = filedialog.asksaveasfile(mode = "w", defaultextension=".txt", title="insert handriting image")
    if file_to_save is None:
        return
    root.deiconify()
    file_to_save.close()
    print(str(file_to_save.name))
    file_to_save = open(file_to_save.name, "w", encoding="utf-8")
    file_to_save.write(result)
    file_to_save.close()


    popup_message("Secceeded, hope to see you again :)", maessage_type(0))

def showResults(root, result):
    global frame_scanned_label, frame, frame_text, frameMarkRun
    frameMarkRun.destroy()
    if  status_program == Status_program(0):
        popup_message("Data insert into the database, goodbye", maessage_type(0))
    else:
        frame_text = Frame(root, relief =  SUNKEN)

        xscrollbar = Scrollbar(frame_text, orient = HORIZONTAL)
        xscrollbar.grid(row = 2, column = 0, sticky = E+W)

        yscrollbar = Scrollbar(frame_text)
        yscrollbar.grid(row = 0, column = 10, sticky = N + S)
        my_result = Text(frame_text, bg = "CadetBlue1", bd = 4, width = 50, xscrollcommand = xscrollbar.set )
        my_result.tag_configure('tag-right', justify='right')
        my_result.insert('end', str(result) , 'tag-right')

        scrl = Scrollbar(root, command=my_result.yview)
        my_result.config(yscrollcommand=scrl.set)
        my_result.grid(row=0, column=0, sticky = N+S+E+W)

        xscrollbar.config(command = my_result.xview)
        yscrollbar.config(command = my_result.yview)

        frame_text.grid(row=5, column=0, columnspan=2)
        #frame_text.grid(row=5, column=0, columnspan=3)

        if status_program == Status_program(0) and scannedInsertDocuments:
            popup_message("Secceeded reading the scanned pages and insert into the Database", maessage_type(0))
        elif status_program == Status_program(0):
            popup_message("Secceeded insert the labeled data into the database", maessage_type(0))
        else:
            popup_message("Finish the export of the text from the image - look at the results :)", maessage_type(0))

        try_again_Button = Button(frame_text, text="Try again", command=lambda: Select_train_test(0)).grid(row=1, column=0,columnspan=2,sticky=W + E)
        save_Button = Button(frame_text, text="Extract result", command=lambda: extractResult(result)).grid(row=2, column=0,columnspan=2,sticky=W + E)

def open_help_window(type):
    top = Toplevel()
    top.title("help")
    top.geometry("400x400")
    if type == Status_program(0):
        txt_file = open(HELP_TEXT_DOC_CREATE, "r")
        #txt_file = open(HELP_TEXT_DOC, "r", encoding="utf-8")
        text = txt_file.read()
        txt_file.close()
    elif type == Status_program(1):
        txt_file = open(HELP_TEXT_DOC_EXTRACT, "r")
        #txt_file = open(HELP_TEXT_DOC, "r", encoding="utf-8")
        text = txt_file.read()
        txt_file.close()

    my_help = Label(top, text=text)
    my_help.pack()
    top.mainloop()


def run_program(finishWrop = False, finishEdit = False):
    global folder_selected, markTextArea, scannedInsertDocuments, root, original_image_array_show
    global images, txtFiles, points, delete_files, images_path_list, images_numpy_array, writerID, isTrain

    isTrain = status_program == Status_program(0)
    if isTrain:
        value = enterID()
        if value == -1:
            Select_train_test(Status_program(1))

    if (not markTextArea):
        if status_program == Status_program(0):
            if scannedInsertDocuments:
                images_path_list, txtFiles = Extract_files_from_folder(folder_selected)
                if images_path_list == []:
                    popup_message("ERROR NO GOOD FILES TO CREATE DATA - CHECK 'help'", maessage_type(2))
                    exit_program(root)
                    exit()
                for i in range(len(images_path_list)):
                    image_array = cv.imread(images_path_list[i], 0)
                    original_image_array.append(image_array.copy())
                    images.append( ImageProcessing.ImageProcessing(original_image_array[i], imagePath=images_path_list[i], handwrite_ID=writerID))
            else:
                EditImage()
                images.append(ImageProcessing.ImageProcessing(original_image_array[0], imagePath=images_path_list[0]))

        # no resize for the selected image
        elif status_program == Status_program(1):
            EditImage()
            images.append(ImageProcessing.ImageProcessing( original_image_array[0], imagePath=images_path_list[0]))

    elif not finishWrop:
        if status_program == Status_program(0):
            if scannedInsertDocuments:
                images_path_list, txtFiles = Extract_files_from_folder(folder_selected,  scannedInsertDocuments)
                if images_path_list == []:
                    popup_message("ERROR NO GOOD FILES TO CREATE DATA - CHECK 'help'", maessage_type(2))
                    exit_program(root)
                    exit()
                for image_path in images_path_list:
                    image_array = cv.imread(image_path, 0)
                    original_image_array.append(image_array.copy())
                    width, height = calculate_width_height(image_array, IMAGE_WIDTH_TO_SHOW, IMAGE_HEIGHT_TO_SHOW)
                    image_array = cv.resize(image_array, (width, height))
                    images_numpy_array_show.append(image_array)
                    imageTK_list.append(ImageTk.PhotoImage(Image.fromarray(image_array)))
                images_numpy_array = original_image_array.copy()
                original_image_array_show = images_numpy_array_show.copy()
                wrap_data()
            else:
                wrap_data()

        elif status_program == Status_program(1):
            wrap_data()

    # after cropp of the images
    else:
        if status_program == Status_program(0):
            for i in range(len(images_path_list)):
                if scannedInsertDocuments:
                    images.append(ImageProcessing.ImageProcessing(images_numpy_array[i], imagePath=images_path_list[i], handwrite_ID=writerID))
                else:
                    EditImage()
                    #images.append(ImageProcessing.ImageProcessing(images_numpy_array[i], imagePath=images_path_list[0], handwrite_ID=writerID))
        elif status_program == Status_program(1):
            EditImage()
            #images.append(ImageProcessing.ImageProcessing(images_numpy_array[0], imagePath=images_path_list[0]))

    print(len(images))
    # for image in images:
    #     cv.imshow("ll", image.imageArray)
    #     cv.waitKey(0)
    print("isTrain"+str(isTrain))
    print("scannedInsertDocuments "+str(scannedInsertDocuments))
    controller = Controller.Controller(isTrain, images, root, isScanned = scannedInsertDocuments)
    result = controller.main()
    showResults(root, result)

def main():
    global folder_selected, markTextArea, scannedInsertDocuments
    global txtFiles, points, delete_files, clicked, root, options, frame , frameExtract, frame_text, frameMarkRun
    reset_global_parameters()
    root = Tk()
    root.title("convert a picture in Hebrew to machine encoded text - Adi Rosenthal")

    frame = Frame(root)
    frame.grid(row=3, column=0,  columnspan = 2 )
    frameExtract = Frame(frame)
    frameExtract.grid(row=5, column=0, columnspan=2)
    frameMarkRun = Frame(root)
    frameMarkRun.grid(row=6, column=0, columnspan=2)
    frame_text = Frame(root, relief=SUNKEN)
    frame_text.grid(row=6, column=0, columnspan=2)
    menubar = Menu(root)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command = root.destroy)
    menubar.add_cascade(label="File", menu=filemenu)

    datamenu = Menu(menubar, tearoff=0)
    datamenu.add_command(label="Check Data", command=lambda: new_window_check_database(root))
    menubar.add_cascade(label="Data", menu=datamenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label = "Help - extract text", command = lambda: open_help_window(Status_program(0)))
    helpmenu.add_command(label = "Help - create data", command = lambda: open_help_window(Status_program(1)))
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)

    options = ["please choose", Status_program(0),Status_program(1)]

    clicked = StringVar()
    clicked.set(options[0])
    myLabel = Label(root, text="Choose one of the options - "+Status_program(0)+" or "+Status_program(1) +":", font=("Ariel", 16))
    drop = OptionMenu(root, clicked, *options, command=Select_train_test)

    myLabel.grid(row=0, column=0, columnspan = 2)
    drop.grid(row=1, column=0, columnspan = 2)

    deleteFiles()
    root.mainloop()

if __name__ == "__main__":
    main()



    # 1) switch case : enum - with all the values
    # 2) print errors with the gui
    # 3) work on the power point - vm, docker ,  vedio -

