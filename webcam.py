# -*- coding: utf-8 -*-
import cv2
import numpy as np


def show_cam(gray=False):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    while True:
        ret, frame = cap.read()
        
        if gray:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow('frame', frame)
        
        k = cv2.waitKey(1)
        
        # Quit if you press the Q or Esc keys
        if k & 0xFF == ord('q'):
            break
        
        elif k == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()


