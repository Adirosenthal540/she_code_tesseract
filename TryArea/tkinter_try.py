from tkinter import *
import cv2 as cv
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import numpy as np
import tkinter.simpledialog
import ImageProcessing
root = Tk()

#setting up a tkinter canvas
img1 = r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\DataBase\316550797_0.tif"
img2 = r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\DataBase\316550797_1.tif"
img3 = r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\DataBase\316550797_2.tif"
img4 = r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\DataBase\316550797_3.tif"


#adding the image
#File = askopenfilename(parent=root, initialdir="./",title='Select an image')
points = []

def click_CutImage(num_image) :
    global points, file, original, img_toCut, cv_array, top2, w, image_list
    top2 = Toplevel()
    top2.title("secend window")
    points = []
    w = Canvas(top2, width=500, height=500)

    img_toCut = image_list[num_image]
    w.create_image(0, 0, image=img_toCut, anchor="nw")
    w.grid(row=0)
    top2.bind("<Button 1>", CutImage)
    print("end cut")

def CutImage(eventorigin):
    global x, y, cv_array, points, cv_array, original, img_toCut, top2, w
    while(len(points)<4):
        x = eventorigin.x
        y = eventorigin.y
        print(x, y)

        cv_array = cv.circle(cv_array, (x, y), 3, 0, -1)
        points.append((x, y))
        if len(points) >= 2:
            cv_array = cv.line(cv_array, points[-1], points[-2], 50, 3)

        original = Image.fromarray(cv_array)
        img_toCut = ImageTk.PhotoImage(original)
        w.create_image(0, 0, image=img_toCut, anchor="nw")

        top2.bind("<Button 1>", CutImage)
        top2.mainloop()
    print (points)
    top2.destroy()

def next_end(image_number):
    global my_image, button_next, button_previous, good_Image, bad_Image, image_list, root_window
    global status, good_Image, image_list
    good_Image.append(image_path_list[image_number])

    status.grid_forget()
    button_next = Button(root_window, text="OK", padx=70, pady=20, state=DISABLED, fg="black",
                           bg="green")
    button_previous = Button(root_window, text="Error", padx=70, pady=20, state=DISABLED, fg="black",
                           bg="red")

    my_image.grid(row=0, column=0, columnspan=3, sticky = W+E)
    button_next.grid(row=1, column=1, sticky = W+E)
    button_previous.grid(row=1, column=2, sticky = W+E)

def back_end(image_number):
    global my_image, button_next, button_previous, status, good_Image, bad_Image, image_list, image_path_list, root_window
    bad_Image.append(image_path_list[image_number])
    my_image.grid_forget()
    button_next = Button(root_window, text="OK", padx=70, pady=20, state=DISABLED, fg="black",
                           bg="green")
    button_previous = Button(root_window, text="Error", padx=70, pady=20, state=DISABLED, fg="black",
                           bg="red")
    my_image.grid(row=0, column=0, columnspan=3)
    button_next.grid(row=1, column=1)
    button_previous.grid(row=1, column=2)

def next( image_number, root):
    global my_image, button_next, button_previous, status, good_Image, bad_Image, image_list, image_path_list, root_window

    # if sign:
    #     good_Image.append(image_path_list[image_number - 1])
    # else:
    #     bad_Image.append(image_path_list[image_number - 1])
    my_image.grid_forget()

    my_image = Label(root, image=image_list[image_number])
    button_next = Button(root_window, text="OK", padx=70, pady=20, command=lambda: next(True, image_number + 1, root),
                           fg="black", bg="green")
    button_previous = Button(root_window, text="Error", padx=70, pady=20,
                           command=lambda: next(False, image_number + 1, root), fg="black", bg="red")
    status = Label(root, text="Image " + str(image_number + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN)

    if image_number == len(image_list) - 1:
        button_next = Button(root_window, text="OK", padx=70, pady=20, command=lambda: eccept(image_number), fg="black",
                               bg="green")
        button_previous = Button(root_window, text="Error", padx=70, pady=20, command=lambda: remove(image_number),
                               fg="black", bg="red")

    my_image.grid(row=0, column=0, columnspan=3)
    button_next.grid(row=1, column=1)
    button_previous.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3)
def back( image_number, root):
    global my_image, button_next, button_previous, status, good_Image, bad_Image, image_list, image_path_list, root_window

    # if sign:
    #     good_Image.append(image_path_list[image_number - 1])
    # else:
    #     bad_Image.append(image_path_list[image_number - 1])
    my_image.grid_forget()

    my_image = Label(root, image=image_list[image_number])
    button_next = Button(root_window, text="OK", padx=70, pady=20, command=lambda: next(True, image_number + 1, root),
                           fg="black", bg="green")
    button_previous = Button(root_window, text="Error", padx=70, pady=20,
                           command=lambda: next(False, image_number + 1, root), fg="black", bg="red")
    status = Label(root, text="Image " + str(image_number + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN)

    if image_number == len(image_list) - 1:
        button_next = Button(root_window, text="OK", padx=70, pady=20, command=lambda: eccept(image_number), fg="black",
                               bg="green")
        button_previous = Button(root_window, text="Error", padx=70, pady=20, command=lambda: remove(image_number),
                               fg="black", bg="red")

    my_image.grid(row=0, column=0, columnspan=3)
    button_next.grid(row=1, column=1)
    button_previous.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3)
def exit_program():
    global root_window, good_Image, bad_Image

    root_window.destroy()



def wrap_data(path_list, root):
    global my_image, image_list, status, image_path_list, root_window
    image_path_list = path_list
    # root = Tk()
    # root.title("Check Data")
    #root.iconbitmap(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\test_images\tesseracticon_dk8_icon.ico")
    root_window = root
    good_Image = []
    bad_Image = []
    image_list = []
    for image_path in path_list:
        image_list.append(ImageTk.PhotoImage(Image.open(image_path)))

    status = Label(root, text = "Image 1 of " + str(len(image_list)), bd =1, relief = SUNKEN)

    my_image = Label(root, image = image_list[0])
    my_image.grid(row = 0, column = 1, columnspan = 3)

    button_exit = Button(root, text = "Exit",padx = 30, pady = 20, command = exit_program)

    button_wrap = Button(root, text = "Cut Image",padx = 30, pady = 20, command = lambda: CutImage(1))

    button_next = Button(root, text="Next", padx=70, pady=20, command=lambda: next( 1, root), fg="black", bg="green")
    button_previous = Button(root, text="Back", padx=70, pady=20, command=lambda: back( 1, root), fg="black", bg="red")


    button_exit.grid(row = 1, column = 0)
    button_next.grid(row = 0, column =2)
    button_previous.grid(row = 0, column = 0)
    status.grid(row=2, column = 0 , columnspan = 3, sticky = W+E)
    root.mainloop()

def new_window_wrap_images(root):
    path_list = [img1, img2, img3, img4]
    top = Toplevel()
    top.title("check database")
    wrap_data(path_list, top)
# myButton = Button(root, text = "", padx = 50, pady = 20, command = lambda: new_window_wrap_images(root), fg = "black", bg = "green")
# myButton.grid(row = 1, column = 0)
new_window_wrap_images()
root.mainloop()