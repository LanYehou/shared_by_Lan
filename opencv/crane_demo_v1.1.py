import cv2 as cv
import numpy as np


def measure_object(src_im):
    src_gray = cv.cvtColor(src_im,cv.COLOR_BGR2GRAY)
    cv.imshow("src_gray", src_gray)
    #ret, src_binary = cv.threshold(src_gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    ret, src_binary = cv.threshold(src_gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("src_binary", src_binary)
    src_dst = cv.cvtColor(src_binary,cv.COLOR_GRAY2RGB)
    contours, heriachy = cv.findContours(src_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)
        x,y,w,h =cv.boundingRect(contour)
        rate = min(w,h)/max(w,h)
        mm = cv.moments(contour)
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        cv.circle(src_im,(np.int(cx),np.int(cy)),3,(0,255,255),-1)
        approxCurve = cv.approxPolyDP(contour,4,True)
        if approxCurve.shape[0] > 6 :
            cv.drawContours(src_im,contours,i,(255,0,255),2)
        if approxCurve.shape[0] == 4:
            cv.drawContours(src_im, contours, i, (0, 255, 255), 2)
        if approxCurve.shape[0] == 3:
            cv.drawContours(src_im, contours, i, (255, 255, 0), 2)
    cv.imshow("out",src_im)

path_im2 = 'images/target1.jpg'
src_im2 = cv.imread(path_im2)
cv.imshow("src_im2",src_im2)
measure_object(src_im2)
cv.waitKey(0)
cv.destroyAllWindows()

