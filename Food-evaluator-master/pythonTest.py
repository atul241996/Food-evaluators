import cv2
import re
import random
import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
import pytesseract as tess
import csv

def imageProcessingFunction(imageName):
 img_con = cv2.imread(imageName,0)
 img = cv2.imread(imageName)

 d = tess.image_to_data(img, output_type=tess.Output.DICT)
 #print(d.keys())

 n_boxes = len(d['text'])
 for i in range(n_boxes):
     if int(d['conf'][i]) > 60:
         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
         img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
  
 cv2.imshow('img',img)
 cv2.waitKey(3000)
 #print(d['text'])
 return d['text']

testInfo = imageProcessingFunction('3.Ashirwad_WF.JPG')
testInfo2 = imageProcessingFunction('3.Pilsbury_WF.JPG')
testInfo1 = imageProcessingFunction('3.Fortune_WF.JPG')

testInfo = list(filter(str.strip, testInfo))
testInfo2 = list(filter(str.strip, testInfo2))
testInfo1 = list(filter(str.strip, testInfo1))

#print(testInfo)
#print(testInfo1)
#print(testInfo2)

def findValues(testInfo,ingredient):
    indexOfIngredient = testInfo.index(ingredient)
    var=''
    for item in testInfo[indexOfIngredient:]:
        if re.match(r'[0-9]',item) is not None:
         #print(item)
         var = item
         break
    return var
    
ingredientValue = findValues(testInfo,'Energy')
ingredientValue1 = findValues(testInfo,'Sugar')
ingredientValue11 = findValues(testInfo,'Protein')
ingredientValue2= findValues(testInfo1,'Sugar')
ingredientValue3= findValues(testInfo1,'Energy')
ingredientValue33= findValues(testInfo1,'Protein')
ingredientValue4= findValues(testInfo2,'Energy')
ingredientValue5= findValues(testInfo2,'Sugar')
ingredientValue55= findValues(testInfo2,'Protein')

#print (ingredientValue)

data = {"Ashirwad":[float(ingredientValue)/10, float(ingredientValue1),float(ingredientValue11[:-1])],"Fortune":[float(ingredientValue3)/10, float(ingredientValue2),float(ingredientValue33)],"Pilsbury":[float(ingredientValue4)/10,float(ingredientValue5)/10,float(ingredientValue55)]};

index     = ["Energy(10Kcal)", "Sugar(g)","Protein(g)"];

dataFrame = pd.DataFrame(data=data, index=index);

dataFrame.plot.bar(rot=15, title="Comparision of ingredients in Atta Brands in 100 g");

plt.show(block=True);

#cv2.imshow('img', img1)
#cv2.waitKey(0)

#img.shape
#thresholding the image to a binary image
#thresh,img_bin = cv2.threshold(img,128,255,cv2.THRESH_BINARY |cv2.THRESH_OTSU)
#inverting the image 
#img_bin = 255-img
#cv2.imwrite('img',img_bin)
#Plotting the image to see the output
#plotting = plt.imshow(img_bin,cmap='gray')
#plt.show()