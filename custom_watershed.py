"""
Program which allows the user to apply the Watershed algorithm with custom
seeds by drawing them on the picture and seeing the result of the algorithm in
another window.

Left click to draw seeds
C to remove all seeds and restart
ESC to quit
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

img_original = cv2.imread('DATA/road_image.jpg')
# img_original = cv2.imread('../faces/images/Meuss.jpg')
"""
img_original = cv2.imread('photo.jpg')
img_original = cv2.resize(img_original,
                          (img_original.shape[0]//2, img_original.shape[1]//2))
"""
img_copy = np.copy(img_original)

marker_img = np.zeros(img_original.shape[:2], dtype=np.int32)
segments = np.zeros(img_original.shape, dtype=np.uint8)

n_markers = 10
current_marker = 1
marks_updated = False

def create_rgb(i):
    return tuple(np.array(cm.tab10(i)[:3])*255)

colors = []
for i in range(10):
    colors.append(create_rgb(i))
    

def mouse_callback(event, x, y, flags, param):
    global marks_updated

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(marker_img, (x, y), 5, (current_marker), -1)
        cv2.circle(img_copy, (x, y), 5, colors[current_marker], -1)
        
        marks_updated = True

cv2.namedWindow('Original')
cv2.setMouseCallback('Original', mouse_callback)

while True:
    cv2.imshow('Watershed Segments', segments)
    cv2.imshow('Original', img_copy)
    
    
    k = cv2.waitKey(1)
    
    # Close if ESC is pressed
    if k == 27:
        break
    
    # Clear colors if C is pressed
    elif k == ord('c'):
        img_copy = img_original.copy()
        marker_img = np.zeros(img_original.shape[:2], dtype=np.int32)
        segments = np.zeros(img_original.shape, dtype=np.uint8)
        marks_updated = False

    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))
        
    elif k == ord('s'):
        cv2.imwrite('../faces/images/meuss_watershed.png', segments)
    
    if marks_updated:
        marker_img_copy = marker_img.copy()
        cv2.watershed(img_original, marker_img_copy)
        segments = np.zeros(img_original.shape, dtype=np.uint8)
        
        for color_id in range(n_markers):
            segments[marker_img_copy == (color_id)] = colors[color_id]
        
        marks_updated = False


cv2.destroyAllWindows()