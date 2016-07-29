import cv2
import numpy as np
import os


def show_methods():
    '''show pattern match methods 
    
    Args: None
    
    Note: there are six pattern match methods provided by OpenCV
    
    Return: None

    '''
    
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    
    for method in methods:
        print method


def pattern_match_coordinate(img2, template, method):
    '''given image and template and pattern match method, return center x, y
    '''
    # methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    
    h, w = template.shape[0], template.shape[1]

    img = img2.copy()

    
    # Apply template Matching
    res = cv2.matchTemplate(img,template,eval(method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # print (min_val, max_val, min_loc, max_loc)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # cv2.rectangle(img,top_left, bottom_right, 255, 4)

    xCenter = top_left[0] + (bottom_right[0] - top_left[0])/2.0
    yCenter = top_left[1] + (bottom_right[1] - top_left[1])/2.0
    # print xCenter, yCenter
    return xCenter, yCenter