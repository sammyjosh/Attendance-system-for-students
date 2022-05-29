# import module from tkinter for UI
from tkinter import *
from playsound import playsound
import os
from datetime import datetime;

# creating instance of TK
root = Tk()

root.configure(background="white")


# root.geometry("300x300")

def function1():
    os.system("py dataset_capture.py")


def function2():
    os.system("py training_dataset.py")


def function3():
    os.system("py recognizer.py")


def function5():
    os.startfile(os.getcwd() + "/developers/diet1frame1first.html");


def function6():
    root.destroy()


def attend():
    os.startfile(os.getcwd() + "/firebase/attendence_filesattendence" + str(datetime.now().date()) + '.xls')


# stting title for the window
root.title("ATTENDENCE SYSTEM FOR STUDENT")

# creating a text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 20), fg="white", bg="green",
      height=2).grid(row=0, rowspan=2, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating first button
Button(root, text="Create Your FaceId:", font=("times new roman", 20), bg="black", fg='white', command=function1).grid(
    row=3, columnspan=2, sticky=W + E + N + S, padx=5, pady=5)

# creating second button
Button(root, text="Train Images", font=("times new roman", 20), bg="black", fg='white', command=function2).grid(
    row=4, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating third button
Button(root, text="Mark your Attendence", font=('times new roman', 20), bg="black", fg="white",
       command=function3).grid(row=5, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating attendance button
Button(root, text="Attendance Sheet", font=('times new roman', 20), bg="black", fg="white", command=attend).grid(
    row=6, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)



Button(root, text="Done", font=('times new roman', 20), bg="red", fg="white", command=function6).grid(row=9,
                                                                                                         columnspan=2,
                                                                                                         sticky=N + E + W + S,
                                                                                                         padx=5, pady=5)

root.mainloop()