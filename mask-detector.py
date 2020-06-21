# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:36:28 2020

@author: SHEINNA
"""
import numpy as np
import imutils
import cv2
import tensorflow as tf
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import os
import time


def select_image():
    global panelA, panelB
    path = filedialog.askopenfilename()
    if len(path) > 0:
        net = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel")
        model = tf.keras.models.load_model('model_mask2.h5', custom_objects=None, compile=True)
        
        image = cv2.imread(path)
        image2 = image
        image = imutils.resize(image, width=300)
        image2 = imutils.resize(image2, width=300)
    
        (h, w) = image2.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image2, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
        net.setInput(blob)
        detections = net.forward()
        
        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence < 0.7:
                continue
            
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            
            crop = image2[startY:endY, startX:endX]
            cropped = Image.fromarray(crop, 'RGB')
            cropped = cropped.resize((150, 150))
            cropped_array = np.array(cropped)
            cropped_array = np.expand_dims(cropped_array, axis=0)
            cropped_array=cropped_array/255
            prediction = model.predict(cropped_array)
            print(prediction)
            if prediction <= 0.1:
                text = "{:.2f}% Unmasked".format(confidence * 100)
                y = startY - 10 if startY - 10 > 10 else startY + 10
                cv2.rectangle(image2, (startX, startY), (endX, endY), (0, 0, 255), 2)
                cv2.putText(image2, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
            else:
                text = "{:.2f}% Masked".format(confidence * 100)
                y = startY - 10 if startY - 10 > 10 else startY + 10
                cv2.rectangle(image2, (startX, startY), (endX, endY), (0, 255, 0), 2)
                cv2.putText(image2, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
                
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image2 = Image.fromarray(image2)
        
        image = ImageTk.PhotoImage(image)
        image2 = ImageTk.PhotoImage(image2)
        
        if panelA is None or panelB is None:
            panelA = tk.Label(image = image)
            panelA.image = image
            panelA.pack(side = "left", padx = 30, pady = 30)
            
            panelB = tk.Label(image = image2)
            panelB.image  = image2
            panelB.pack(side = "right", padx = 30, pady = 30)
            
        else:
            panelA.configure(image = image)
            panelB.configure(image = image2)
            panelA.image = image
            panelB.image = image2 

window = tk.Tk()
panelA = None
panelB = None

greeting = tk.Label(
    text = "Welcome to the Mask Detector",
    font = ("Courier", 18),
    width = 30,
    foreground = "white",
    background = "black"
    )

def startVideoTest():
    os.system('python detect_mask.py')

def startWebCamDetection():
    os.system('python detect_mask.py')

buttonImage = tk.Button(
    text = "Select an image",
    command = select_image,
    width = 25,
    height = 3,
    bg = "purple",
    fg = "white"
    )

greeting.pack(
    side = "top", 
    fill = "both",
    expand = "yes",
    padx = "10",
    pady = "10"
    )

buttonImage.pack(
    padx = "10",
    pady = "5"
    )

window.mainloop()