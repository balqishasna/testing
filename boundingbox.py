import cv2
from numpy import angle
from detector import *
import numpy as np
import time
import csv
from bdb import effective
import math

img = cv2.imread("D:\Kuliah\judul-skripsi\codingan\Percobaan\output\hasil_10.png")

list_rect = []

detector = HomogeneousBgDetector()

contours = detector.detect_objects(img)

header = ['file_name', 'x', 'y', 'width' , 'height', 'angle']

with open('data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

for cnt in contours:
    # Get rect
    rect = cv2.minAreaRect(cnt)
    (x, y), (w , h), angle = rect
    print (rect)

    file_name = "hasil_{}.jpg".format(int(time.time()))
    data = []

    data.extend([file_name, w, h])

#cropping
    list_rect.append(rect)

    print(list_rect, len(list_rect))
    for item in range(len(list_rect)):
      (x, y), (w , h), angle = list_rect[item]
      X = int(math.ceil(x))
      Y = int(math.ceil(y))
      W = int(math.ceil(w))
      H = int(math.ceil(h))
      #cropped_image = img[Y:Y+H, X:X+W]
      print(X,Y,W,H)
     # cropped_image = img[X:X+W, Y:Y+H]
      # print([x,y,w,h])
      
    with open('data.csv', 'a+', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the data
        writer.writerow(data)
 
    # display rectangle
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)

#disini buat brightness nya
def apply_brightness_contrast(input_img, img, brightness = 0, contrast = 0):

fcolor = (0,0,0)
font = cv2.FONT_HERSHEY_SIMPLEX

blist = [-10] # list of brightness values-10
clist = [112] # list of contrast values122

#rasio
out = np.zeros((s*1, s*1, 3), dtype = np.uint8)

for i, b in enumerate(blist):
    c = clist[i]
    print('b, c:  ', b,', ',c)
    row = s*int(i/3)
    col = s*(i%3)
    
    print('row, col:   ', row, ', ', col)
    
    out[row:row+s, col:col+s] = apply_brightness_contrast(img, b, c)
    msg = 'b %d' % b
    cv2.putText(out,msg,(col,row+s-22), font, .7, fcolor,1,cv2.LINE_AA)
    msg = 'c %d' % c
    cv2.putText(out,msg,(col,row+s-4), font, .7, fcolor,1,cv2.LINE_AA)
    
    #cv2.putText(out,(260,30), font, 1.0, fcolor,2,cv2.LINE_AA)

#click 'q' to save
cv2.imshow('Effect', out)
k = cv2.waitKey(0) & 0xFF
if k == ord('q'):
     #cv2.imwrite("D:\Kuliah\judul-skripsi\codingan\contrast\percobaan\output\hasil3_416_{0,75}.jpg".format(int(time.time())), out)
     cv2.imwrite('D:\Kuliah\judul-skripsi\codingan\Percobaan\output\hasill_10.jpg', out)