#!/bin/python
from PIL import Image
import os

source = None
maxWight = None

def read1():
    global source
    source = input("Select file: ")
    if not os.path.isfile(source):
        read1()

def read2():
    global maxWight
    maxWight = input("Select size (150 by default): ")
    if maxWight == "":
        maxWight = 150
    elif not isinstance(maxWight, int):
        read2()

read1()
read2()

symbs = [".",",",":","+","*","?","%","$","#","@"]

def mapp(val,start1,stop1,start2,stop2):
    return ((val-start1)/(stop1-start1))*(stop2-start2)+start2

img = Image.open(source)
text = ""
coufHeight = 0.5

with open("ascii_" + source, "w") as fl:
    newHeight = int(img.size[1]/coufHeight*maxWight/img.size[0])
    if img.size[0] > maxWight or img.size[1] > newHeight:
        img.thumbnail((maxWight,int(newHeight)))
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            r, g, b = img.getpixel((x,y))
            gray = int(r*0.2126+g*0.7152+b*0.0722)
            mapIndex = mapp(gray,0,255,0,len(symbs))
            text += symbs[int(mapIndex)]
        fl.write(text + "\n")
        text = ""
