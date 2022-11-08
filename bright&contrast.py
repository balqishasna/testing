import cv2
import numpy as np

# Open a typical 24 bit color image. For this kind of image there are
# 8 bits (0 to 255) per color channel
img = cv2.imread('D:\Kuliah\judul-skripsi\codingan\Percobaan\uji\hari5_10b.jpg') # mandrill reference image from USC SIPI

s = 1024
# img = cv2.resize(img, (s,s), 0, 0, cv2.INTER_AREA)

def apply_brightness_contrast(input_img, img, brightness = 0, contrast = 0):
    
    # img = cv2.imread('D:\Kuliah\judul-skripsi\codingan\Percobaan\uji\hari5_10b.jpg')
    img = cv2.resize(img, (s,s), 0, 0, cv2.INTER_AREA)
    
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow
        
        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()
    
    if contrast != 0:
        f = 131*(contrast + 127)/(127*(131-contrast))
        alpha_c = f
        gamma_c = 127*(1-f)
        
        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf

# font = cv2.FONT_HERSHEY_SIMPLEX
# fcolor = (0,0,0)

# blist = [-15] # list of brightness values
# clist = [127] # list of contrast values

# out = np.zeros((s*1, s*1, 3), dtype = np.uint8)

# for i, b in enumerate(blist):
#     c = clist[i]
#     print('b, c:  ', b,', ',c)
#     row = s*int(i/3)
#     col = s*(i%3)
    
#     print('row, col:   ', row, ', ', col)
    
#     out[row:row+s, col:col+s] = apply_brightness_contrast(img, b, c)
#     msg = 'b %d' % b
#     cv2.putText(out,msg,(col,row+s-22), font, .7, fcolor,1,cv2.LINE_AA)
#     msg = 'c %d' % c
#     cv2.putText(out,msg,(col,row+s-4), font, .7, fcolor,1,cv2.LINE_AA)
    
#     cv2.putText(out, 'OpenCV',(260,30), font, 1.0, fcolor,2,cv2.LINE_AA)

# cv2.imwrite('D:\Kuliah\judul-skripsi\codingan\Percobaan\hasil_10b.png', out)