import cv2 as cv
import numpy as np

vid = cv.VideoCapture("0001-0601.mp4", 0)


#Dimensions of video frame
width = int(vid.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(vid.get(cv.CAP_PROP_FRAME_HEIGHT))

aspect = width/height

new_h = 720
new_w = new_h * aspect
while True:

    
    ret, frame = vid.read()
    
    #Resize frame while maintaining ratio
    # Python program to compute and visualize the

    #Convert color to HSV 
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #Convert to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #Range of green in HSV coordinates
    lower_green = np.array([45,70,10])
    upper_green = np.array([100,255,255])

    #Range of purp in HSV coordinates
    lower_purp = np.array([135,70,150])
    upper_purp = np.array([170,255,255])
    
    #Range of blue
    lower_blue = np.array([90,100,150])
    upper_blue = np.array([135,255,255])
    #Mask the ranges of color in vid
    mask_green = cv.inRange(hsv, lower_green, upper_green)
    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)
    mask_purp = cv.inRange(hsv, lower_purp, upper_purp)
    #Combine the lower and upper red masks
    mask_all = mask_green + mask_blue + mask_purp

    
    #masked_color = cv.bitwise_and(frame, frame, mask=mask_all)

    gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)                 #Make grayscale image a 3-channel image
    color_overlay_grayscale = np.where(mask_all[..., None] != 0,    #Keep color where mask is white
                              frame,                                #original pixel color
                              gray_bgr)  

    


    while True:
        
        cv.imshow('Color Mask', color_overlay_grayscale)   
        cv.imshow('Masked', mask_all)
        cv.imshow('Grayscale', gray)
        cv.imshow('Original', frame)
        if cv.waitKey(1) != ord('q'):
            break 

vid.release()
cv.destroyAllWindows
