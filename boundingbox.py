import cv2
from numpy import angle
from detector import *
import numpy as np
import time
import csv
from bdb import effective
import math
from brightncontrast import *

img = cv2.imread("D:\Kuliah\judul-skripsi\codingan\Percobaan\output\hasil_10.png")

#image crop
# y=400
# x=210
# h=800
# w=260
# crop_image = img[x:w, y:h]
# cv2.imshow("Croped", crop_image)
# #cv2.waitKey(0)

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
    # cv2.putText(img, "Width {} px".format(round(w, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 1.5, (100, 200, 0), 1)
    # cv2.putText(img, "Height {} px".format(round(h, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 1.5, (100, 200, 0), 1) 

# def BrightnessContrast(brightness=0):
  
#   # getTrackbarPos returns the current
#   # position of the specified trackbar.
#   brightness = cv2.getTrackbarPos('Brightness',
#                   'GEEK')
  
#   contrast = cv2.getTrackbarPos('Contrast',
#                 'GEEK')

#   effect = controller(img, brightness,
#             contrast)

#automation brightness
s = 1024
# img = cv2.resize(img, (s,s), 0, 0, cv2.INTER_AREA)
def apply_brightness_contrast(input_img, img, brightness = 0, contrast = 0):

# def controller(input_img, brightness = 0, contrast = 0):

#     if brightness != 0:

#         if brightness > 0:
#            shadow = brightness
#            max = 255
#         else:
#            shadow = 0
#            max = 255 + brightness
#         al_pha = (max - shadow) / 255
#         ga_mma = shadow

#         buf = cv2.addWeighted(input_img, al_pha, input_img, 0, ga_mma)
#     else:
#         buf = input_img.copy()

#     if contrast != 0:
#         f = 131*(contrast + 127)/(127*(131-contrast))
#         alpha_c = f
#         gamma_c = 127*(1-f)
        
#         buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

#     return buf

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