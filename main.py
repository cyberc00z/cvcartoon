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
                                      
    # convert image into grayscale 
    grayScale = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    r2 = cv2.resize(grayScale,(960,540))

    #applying median blur to smoothen image
    smoothGrayScale = cv2.medianBlur(grayScale,5)
    r3 = cv2.resize(smoothGrayScale,(960,540))

    #reteriving the edges for effect
    getEdge = cv2.adaptiveThreshold(smoothGrayScale,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9,9)
    r4 = cv2.resize(getEdge, (960,540))
    
    # applying bilateral filter 
    colorImage = cv2.bilateralFilter(originalImage,9,300,300)
    r5 = cv2.resize(colorImage, (960,540))

    #masking edges image with our final image
    finalImage = cv2.bitwise_and(colorImage,colorImage,mask=getEdge)
    r6 = cv2.resize(finalImage,(960,540))
     
    images = [r1,r2,r3,r4,r5,r6]
    fig,axes = plt.subplots(3,2,figsize=(8,0),subplot_kw={'xticks':[],'yticks':[]},gridspec_kw=dict(hspace=0.1,wspace=0.1))

    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')
    save1 = tk.Button(top, text="Save Catoon Image ", command=lambda:saveImage(ImagePath, r4),padx=30,pady=5)
    save1.configure(background='#364156',foreground='white', font={'calibri',10, 'bold'})
    save1.pack(side=TOP, pady=50)
    plt.show()


def uploadBox():
    ImagePath = easygui.fileopenbox()
    changeToCartoon(ImagePath)


def saveImage(ImagePath,r2):
    name = "cartoon_image"
    path1 = os.path.dirname(ImagePath)
    ext = os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, name + ext)
    cv2.imwrite(path,cv2.cvtColor(r2,cv2.COLOR_BGR2RGB))
    mes = "save by name" + name + "at path" + path
    tk.messagebox.showinfo(title=None, message=mes)


upload = tk.Button(top, text= " Choose an Image Please", command=uploadBox,padx=10,pady=5)
upload.configure(background='#364156',foreground='white', font=('calibri', 10, 'bold'))
upload.pack(side=TOP, pady=50)

top.mainloop()

