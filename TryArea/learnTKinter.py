from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import cv2 as cv
# # 1
# root = Tk()
#
# myLabel = Label(root, text = "hello world")
#
# myLabel.pack()
#
# root.mainloop()

# # 2
# root = Tk()
# myLabel = Label(root, text = "hello world")
# myLabe2 = Label(root, text = "my name is Adi")
#
# myLabel.grid(row = 0, column = 0)
# myLabe2.grid(row = 1, column = 1)
#
# root.mainloop()

# # 3
#
# root = Tk()
#
# def MyClick():
#     myLabel = Label(root, text = "I clicked")
#     myLabel.pack()
#
# myButton = Button(root, text = "Click", padx = 50, pady = 20, command = MyClick, fg = "black", bg = "green")
# myButton.pack()
#
# root.mainloop()

# # 4
#
# root = Tk()
#
# e = Entry(root, width = 50, borderwidth = 5)
# e.pack()
# #e.insert(0, "Enter your name : ")
# def MyClick():
#     myLabel = Label(root, text ="hello " + e.get())
#     myLabel.pack()
#
# myButton = Button(root, text = "enter your name", padx = 50, pady = 20, command = MyClick, fg = "black", bg = "green")
# myButton.pack()
#
# root.mainloop()

# # 5
#
# root = Tk()
# root.title("title")
# e = Entry(root, width = 35, borderwidth = 5)
# e.grid(row = 0, column = 0, columnspan=3, padx=10, pady=10)
# action = "plus"
# f_num = None
# def button_click(number):
#     #e.delete(0,END)
#     current = e.get()
#     e.insert(len(current), number)
#
# def button_clear():
#     e.delete(0, END)
#
# def button_add():
#     first_num = e.get()
#     global f_num, action
#     if f_num!= None:
#         f_num = f_num + int(first_num)
#     else:
#         f_num = int(first_num)
#     e.delete(0, END)
#     action = "plus"
#
# def button_equal():
#     second_num = e.get()
#     e.delete(0, END)
#     if action == "plus":
#         e.insert(0, f_num + int(second_num))
#
# button1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
# button2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
# button3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
# button4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
# button5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
# button6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
# button7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
# button8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
# button9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
# button0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
# button_add = Button(root, text = "+", padx = 40, pady = 20, command = button_add)
# button_equal = Button(root, text = "=", padx = 91, pady = 20, command = button_equal)
# button_clear = Button(root, text = "Clear", padx = 79, pady = 20, command = button_clear)
#
#
# button1.grid(row = 3, column = 0)
# button2.grid(row = 3, column = 1)
# button3.grid(row = 3, column = 2)
#
# button4.grid(row = 2, column = 0)
# button5.grid(row = 2, column = 1)
# button6.grid(row = 2, column = 2)
#
# button7.grid(row = 1, column = 0)
# button8.grid(row = 1, column = 1)
# button9.grid(row = 1, column = 2)
#
# button0.grid(row = 4, column = 0)
#
# button_add.grid(row = 5, column = 0)
# button_equal.grid(row = 5, column = 1,  columnspan=2)
# button_clear.grid(row = 4, column = 1,  columnspan=2)
#
# root.mainloop()

#
# # 6
#
# root = Tk()
# root.title("course part 6")
# root.iconbitmap(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\test_images\tesseracticon_dk8_icon.ico")
# good_Image = []
# bad_Image = []
# img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\DataBase\316550797_0.tif"))
# img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\DataBase\316550797_1.tif"))
# img3 = ImageTk.PhotoImage(Image.open(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\DataBase\316550797_2.tif"))
# img4 = ImageTk.PhotoImage(Image.open(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\DataBase\316550797_3.tif"))
#
# image_list = [img1, img2, img3, img4]
# status = Label(root, text = "Image 1 of " + str(len(image_list)), bd =1, relief = SUNKEN)
# def eccept(image_number):
#     global my_label
#     global button_eccept
#     global button_remove
#     global status
#     good_Image.append(image_list[image_number])
#
#     status.grid_forget()
#     button_eccept = Button(root, text="OK", padx=70, pady=20, state = DISABLED, fg="black",
#                            bg="green")
#     button_remove = Button(root, text="Error", padx=70, pady=20, state = DISABLED, fg="black",
#                            bg="red")
#
#     my_label.grid(row = 0, column = 0, columnspan = 3)
#     button_eccept.grid(row = 1, column = 1)
#     button_remove.grid(row = 1, column = 2)
#
# def remove(image_number):
#     global my_label
#     global button_eccept
#     global button_remove
#     global status
#     bad_Image.append(image_list[image_number])
#     my_label.grid_forget()
#     button_eccept = Button(root, text="OK", padx=70, pady=20, state = DISABLED, fg="black",
#                            bg="green")
#     button_remove = Button(root, text="Error", padx=70, pady=20, state = DISABLED, fg="black",
#                            bg="red")
#     my_label.grid(row = 0, column = 0, columnspan = 3)
#     button_eccept.grid(row = 1, column = 1)
#     button_remove.grid(row = 1, column = 2)
#
# def foward(sign, image_number):
#     global my_label
#     global button_eccept
#     global button_remove, status
#
#     if sign:
#         good_Image.append(image_list[image_number-1])
#     else:
#         bad_Image.append(image_list[image_number-1])
#
#     my_label.grid_forget()
#
#     my_label = Label(image=image_list[image_number])
#     button_eccept = Button(root, text="OK", padx=70, pady=20, command= lambda: foward(True, image_number + 1),
#                            fg="black", bg="green")
#     button_remove = Button(root, text="Error", padx=70, pady=20,
#                            command=lambda: foward(False, image_number +1), fg="black", bg="red")
#     status = Label(root, text="Image " + str(image_number + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN)
#
#     if image_number == len(image_list) -1:
#         button_eccept = Button(root, text="OK", padx=70, pady=20, command=lambda: eccept(image_number), fg="black", bg="green")
#         button_remove = Button(root, text="Error", padx=70, pady=20, command=lambda: remove(image_number), fg="black", bg="red")
#
#     my_label.grid(row = 0, column = 0, columnspan = 3)
#     button_eccept.grid(row = 1, column = 1)
#     button_remove.grid(row = 1, column = 2)
#     status.grid(row=2, column=0, columnspan=3)
#
# def exit_program():
#     print(good_Image)
#     print(bad_Image)
#     root.quit()
#
# my_label = Label(image = img1)
# my_label.grid(row = 0, column = 0, columnspan = 3)
#
# # button_back = Button(root, text = "<<", command = lambda: back(1))
# # button_foward = Button(root, text = ">>", command = lambda: foward(1))
# button_exit = Button(root, text = "Exit",padx = 30, pady = 20, command = exit_program)
#
# button_eccept = Button(root, text="OK", padx=70, pady=20, command=lambda: foward(True, 1), fg="black", bg="green")
# button_remove = Button(root, text="Error", padx=70, pady=20, command=lambda: foward(False, 1), fg="black", bg="red")
# # button_back.grid(row = 0, column = 0)
# # button_foward.grid(row = 0, column = 3)
# button_exit.grid(row = 1, column = 0)
# button_eccept.grid(row = 1, column = 1)
# button_remove.grid(row = 1, column = 2)
# status.grid(row=2, column = 0 , columnspan = 3, sticky = W+E)
# root.mainloop()


# # 7
#
# root = Tk()
# root.title("course part 6")
# root.iconbitmap(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\test_images\tesseracticon_dk8_icon.ico")
#
# frame = LabelFrame(root, text = "this is my frame", padx = 100, pady = 100)
# frame.pack(padx = 10, pady = 10)
#
# b = Button(frame, text = "dont click")
# b.grid(row = 0, column = 0)
# b = Button(frame, text = "dont click2")
# b.grid(row = 1, column = 0)
# root.mainloop()
#
# # 8
#
# root = Tk()
# root.title("course part 8")
# root.iconbitmap(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\test_images\tesseracticon_dk8_icon.ico")
#
# r = IntVar()
# r.set("2")
# def clicked(value):
#     mylabel = Label(root, text=value)
#     mylabel.pack()
# Radiobutton(root, text = "option 1", variable = r, value = 1, command = lambda:clicked(r.get())).pack()
# Radiobutton(root, text = "option 2", variable = r, value = 2, command = lambda:clicked(r.get())).pack()
#
# mylabel = Label(root, text = r.get())
# mylabel.pack()
#
# myButton = Button(root, text = "Click me!" ,command = lambda:clicked(r.get()))
#
# myButton.pack()
# root.mainloop()


# # 9
#
# root = Tk()
# root.title("course part 8")
# root.iconbitmap(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\test_images\tesseracticon_dk8_icon.ico")
# # showinfo, showerror, showwarning, askokcancel, askyesno
# def popup():
#     response = messagebox.askyesno("This is my popup", "Hello")
#     #Label(root, text = response).pack()
#     if response ==1:
#         Label(root, text="you click yes").pack()
#     else:
#         Label(root, text="you click no").pack()
#
#
# Button(root, text = "Popup", command = popup).pack()
#
# root.mainloop()

# # 9
#
# root = Tk()
# root.title("course part 8")
# root.iconbitmap(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\test_images\tesseracticon_dk8_icon.ico")
#
# def open():
#     global my_img, my_label
#     top = Toplevel()
#     top.title("secend window")
#     my_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\DataBase\316550797_2.tif"))
#     my_label = Label(top, image = my_img).pack()
#     btn2 = Button(top, text = "close window", command = top.destroy).pack()
#
# btn = Button(root, text = "Open second window", command = open).pack()
# mainloop()

# 10
#
# root = Tk()
# root.title("course part 8")
# root.geometry("500x500")
# root.iconbitmap(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\test_images\tesseracticon_dk8_icon.ico")
# folderName = r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\handwriteDoc\train_songs\testPDF2"

# def open():
#     global my_img
#     root.filename = filedialog.askopenfilename( title = "select a file", filetype = (("all files", "*.*") , ("PNG", "*.png"), ("TIF", "*.tif")))
#     my_label = Label(root, text = root.filename).pack()
#     my_img = ImageTk.PhotoImage(Image.open(root.filename))
#     my_image_label = Label( image = my_img).pack()
#     # root.withdraw()
#     # folder_selected = filedialog.askdirectory()
#     # print(folder_selected)
#
# my_btn = Button(root, text = "Open file", command = open).pack()
# mainloop()
# # 11
#
# root = Tk()
# root.title("course part 8")
# root.geometry("500x500")
# root.iconbitmap(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\test_images\tesseracticon_dk8_icon.ico")
# def slide():
#     my_label = Label(root, text=horizontal.get()).pack()
#     root.geometry(str(vertical.get())+"x500")
#
# vertical = Scale(root, from_ = 0, to = 400)
# vertical.pack()
# horizontal = Scale(root, from_ =  0, to =  400, orient = HORIZONTAL)
# horizontal.pack()
# my_label = Label(root, text = vertical.get()).pack()
#
#
# my_btn = Button(root, text = "click me", command = slide).pack()
# root.mainloop()

# 12
#
# root = Tk()
# root.title("course part 8")
# root.geometry("500x500")
# #root.iconbitmap(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\test_images\tesseracticon_dk8_icon.ico")
#
# def show():
#     myLable = Label(root, text=var.get()).pack()
# var = StringVar()
# c = Checkbutton(root, text = "check this box", variable = var, onvalue = "On", offvalue = "Off")
# c.deselect()
# c.pack()
#
#
# my_btn = Button(root, text = "shoe selection", command = show).pack()
# root.mainloop()

# # 13
#
# root = Tk()
# root.title("course part 8")
# root.geometry("500x500")
# #root.iconbitmap(r"C:\Users\Adi Rosental\Documents\she_code\shecode_final_project\test_images\tesseracticon_dk8_icon.ico")
#
# def show(var):
#     global myLabel
#     myLabel.grid_forget()
#     value = clicked.get()
#     myLabel = Label(root, text=value)
#     if value =="Train":
#         myLabel= Label(root, text="ask something")
#     if value == "Test":
#         myLabel = Label(root, text="blabla")
#     myLabel.grid(row=1, column=0, columnspan=3)
#
#
# global myLabel
# options = ["-", "Train", "Test"]
#
# clicked = StringVar()
# clicked.set(options[0])
# myLabel = Label(root, text=clicked.get())
# myLable2 = Label(root, text=" ")
# drop = OptionMenu(root, clicked, *options, command = show)
# #drop.pack()
# drop.grid(row = 0, column = 0, columnspan = 3)
# myLabel.grid(row = 1, column = 0, columnspan = 3)
#
# #my_btn = Button(root, text = "show selection", command = show).pack()
# root.mainloop()
#
#
# def donothing():
#    print ("a")
#
# def file_save():
#     pass
#
# root = Tk()
# root.geometry("500x500")
# menubar=Menu(root)
# text=Text(root)
# text.pack()
# filemenu=Menu(menubar,tearoff=0)
# filemenu.add_command(label="New", command=donothing)
# filemenu.add_command(label="Open", command=donothing)
# filemenu.add_command(label="Save", command=file_save)
# filemenu.add_command(label="Save as...", command=donothing)
# filemenu.add_command(label="Close", command=donothing)
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=filemenu)
#
# editmenu=Menu(menubar,tearoff=0)
# editmenu.add_command(label="Undo", command=donothing)
# editmenu.add_command(label="Copy", command=donothing)
# editmenu.add_command(label="Paste", command=donothing)
# menubar.add_cascade(label="Edit", menu=editmenu)
#
# helpmenu=Menu(menubar,tearoff=0)
# helpmenu.add_command(label="Help",command=donothing)
# menubar.add_cascade(label="Help",menu=helpmenu)
#
# root.config(menu=menubar)
# root.mainloop()


#
# event2canvas = lambda e, c: (c.canvasx(e.x), c.canvasy(e.y))
#
# if __name__ == "__main__":
#     root = Tk()
#
#     # setting up a tkinter canvas with scrollbars
#     frame = Frame(root, bd=2, relief=SUNKEN)
#     frame.grid_rowconfigure(0, weight=1)
#     frame.grid_columnconfigure(0, weight=1)
#     xscroll = Scrollbar(frame, orient=HORIZONTAL)
#     xscroll.grid(row=1, column=0, sticky=E + W)
#     yscroll = Scrollbar(frame)
#     yscroll.grid(row=0, column=1, sticky=N + S)
#     canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
#     canvas.grid(row=0, column=0, sticky=N + S + E + W)
#     xscroll.config(command=canvas.xview)
#     yscroll.config(command=canvas.yview)
#     frame.pack(fill=BOTH, expand=1)
#
#     # adding the image
#     File = filedialog.askopenfilename(parent=root, initialdir="C:/", title='Choose an image.')
#     print("opening %s" % File)
#     img = PhotoImage(file=File)
#     canvas.create_image(0, 0, image=img, anchor="nw")
#     canvas.config(scrollregion=canvas.bbox(ALL))
#
#
#     # function to be called when mouse is clicked
#     def printcoords(event):
#         # outputting x and y coords to console
#         cx, cy = event2canvas(event, canvas)
#         print("(%d, %d) / (%d, %d)" % (event.x, event.y, cx, cy))
#
#
#     # mouseclick event
#     canvas.bind("<ButtonPress-1>", printcoords)
#     canvas.bind("<ButtonRelease-1>", printcoords)
#
#     root.mainloop()