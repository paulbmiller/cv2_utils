"""
Script to draw a red circle on an image dynamically with the left click.
"""

import cv2
import numpy as np
from PIL import Image
img = cv2.imread('test.jpg')
# img = cv2.resize(img, (img.shape[0]//2, img.shape[1]//2))


THICKNESS = 2
RED = (0, 0, 255)

curr_img = np.copy(img)
final_img = np.copy(img)
drawing = False
x0 = -1
y0 = -1


def draw_circ(event, x, y, flags, param):
    global drawing, x0, y0, final_img, curr_img
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x0 = x
        y0 = y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if x > x0:
                radius = int((x-x0)/2)
            else:
                radius = int((x0-x)/2)
            
            mask = np.zeros(img.shape, dtype=np.uint8)
            cv2.circle(mask, center=(int((x+x0)/2), int((y+y0)/2)),
                       radius=radius, color=RED, thickness=THICKNESS)
            final_img = cv2.add(src1=curr_img, src2=mask, dst=final_img)
    
    elif event == cv2.EVENT_LBUTTONUP:
        curr_img = np.copy(final_img)
        drawing = False

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_circ)

while True:
    cv2.imshow('my_drawing', final_img)
    
    # quit if Esc is pressed
    if cv2.waitKey(20) & 0xFF == 27:
        break
    
    if cv2.waitKey(20) & 0xFF == ord('c'):
        curr_img = np.copy(img)
        final_img = np.copy(img)
        
    if cv2.waitKey(20) & 0xFF == ord('s'):
        im = Image.fromarray(final_img)
        im.save('out.jpg')

cv2.destroyAllWindows()