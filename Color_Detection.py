#importing libraries
import cv2 as cv
import pandas as pd
import numpy as np

#taking an image from user
path = input("please enter the path for the image")
img = cv.imread(path)

#Declaring var
clicked = False
r = g = b = 0
xpos = ypos = 0

#Read csv file
index = ["color","color_name","hex","R","G","B"]
colors_csv = pd.read_csv("C:/Users/SriSaiRam/Desktop/Prg/colors.csv", names = index, header = None)


#Calcuate distance
def getColorCode(R,G,B):
    min_val = 10000
    for i in range(len(colors_csv)):
        d = abs(R-int(colors_csv.loc[i,"R"])) + abs(G-int(colors_csv.loc[i,"G"])) + abs(B-int(colors_csv.loc[i,"B"]))
        if(d<=min_val):
            min_val = d
            color_name = colors_csv.loc[i,"color_name"]
    return color_name

#ClickFunction
def click_func(event, x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

#Mouse callback event
cv.namedWindow('ColoredImage')
cv.setMouseCallback('ColoredImage', click_func)

while(1):
    cv.imshow("ColoredImage",img)
    if (clicked):
        #cv2.rectangle(image, startpoint, endpoint, color, thickness) -1 thickness fills rectangle entirely
        cv.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        #Creating text string to display ( Color name and RGB values )
        text = getColorCode(r,g,b) + ' R='+ str(r) + ' G='+ str(g) + ' B='+ str(b)
        #cv2.putText(img,text,start,font(0-7), fontScale, color, thickness, lineType, (optional bottomLeft bool) )
        cv.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv.LINE_AA)
  #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv.LINE_AA)
        clicked=False
    #Break the loop when user hits 'esc' key 
    if cv.waitKey(20) & 0xFF ==27:
        break
cv.destroyAllWindows()

