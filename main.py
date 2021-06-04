import os ,sys
import cv2
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image
from numpy.lib.arraypad import pad
import easygui

top = tk.Tk()
top.geometry('500x500')
top.title('Cartoonifying Images')
top.configure(background='white')
label = Label(top, background='#CDCDCD', font=('calibri', 20, 'bold'))


def changeToCartoon(ImagePath):
    originalImage = cv2.imread(ImagePath)
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)

    if originalImage is None:
        print("Please Choose a Valid File.")
        sys.exit(0)

    r1 = cv2.resize(originalImage, (960, 540))
    plt.imshow(r1, cmap='gray')



def uploadBox():
    path = easygui.fileopenbox()
    changeToCartoon(ImagePath)

upload = tk.Button(top, text= " Choose a Image Please", command=uploadBox,padx=10,pady=5)
upload.configure(background='#364156',foreground='white', font=('calibri', 10, 'bold'))
upload.pack(side=TOP, pady=50)

top.mainloop()

