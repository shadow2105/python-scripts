#!/usr/bin/python3

import sys
import pandas
import numpy as np  
import cv2
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

#Reading the data file to generate wordcloud for 
file = sys.argv[1]
dataset = open(file, "r").read()

image_mask = sys.argv[2]
image_wordCloud = sys.argv[3]

#function to generate wordcloud
def create_wordCloud(text):
   mask_array = np.array(Image.open(image_mask))
   cloud = WordCloud(background_color = "white", max_words = 200, mask = mask_array, contour_width = 15, stopwords = set(STOPWORDS))
   cloud.generate(text)
   cloud.to_file(image_wordCloud)

dataset = dataset.lower()
create_wordCloud(dataset)

#path of image specified as a command line argument
image = sys.argv[3]

#Reading the image with opencv
img = cv2.imread(image)

#Reading csv file with pandas and giving names to each column to create a DataFrame
index=["color","color_name","hex","R","G","B"]
csv = pandas.read_csv('colors.csv', names = index, header = None)
print("Size of DataFrame (Number of rows in csv file): {}\n".format(len(csv)))

#declaring global variables
clicked = False
r = g = b = xpos = ypos = 0

#function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:              #left button double click
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]                              #R, G, B value of pixel at (x, y) coordinate
        b = int(b)
        g = int(g)
        r = int(r)
        print("[{}]\n(R, G, B): {}	(x, y): {}\n".format(getColorName(r,g,b),(r,g,b), (xpos, ypos)))

#function to calculate minimum distance from all colors in the DataFrame and get the most matching color
#d = abs(Red – ith RedColor) + abs(Green – ith GreenColor) + abs(Blue – ith BlueColor)
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        dR = abs(R - int(csv.loc[i,"R"]))              #column "R" of the ith row of DataFrame
        dG = abs(G - int(csv.loc[i,"G"]))              #column "G" of the ith row of DataFrame
        dB = abs(B - int(csv.loc[i,"B"]))              #column "B" of the ith row of DataFrame
        d = dR + dG + dB
        if(d <= minimum):
            minimum = d
            color_name = csv.loc[i,"color_name"]
    return color_name

cv2.namedWindow('image', cv2.WINDOW_NORMAL)            #placeholder for cv2.imshow
cv2.setMouseCallback('image',draw_function)

while(1):

    cv2.imshow("image", img)
    if (clicked):
   
        #cv2.rectangle(image, startpoint, endpoint, color, thickness): thickness = -1 fills the entire rectangle 
        cv2.rectangle(img, (20,20), (750,60), (b,g,r), -1)

        #Creating text string to display( Color name and RGB values )
        text = '[' + getColorName(r,g,b) + ']    ' + '  (R, G, B) = '+ '(' + str(r) + ', ' + str(g) + ', ' + str(b) +  ')'
        
        #cv2.putText(img, text, start, font(0-7), fontScale, color, thickness, lineType )
        cv2.putText(img, text, (50,50), 4, 0.6, (255,255,255), 1, cv2.LINE_AA)

        #For very light colours we will display text in black colour
        if(r + g + b >= 600):
            cv2.putText(img, text, (50,50), 4, 0.6, (0,0,0), 1, cv2.LINE_AA)
            
        clicked=False
        
    #Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()



