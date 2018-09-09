import cv2, glob 
import numpy
images=glob.glob("*.JPG")

for image in images:
    img=cv2.imread(image,0)
    cv2.imshow('image',img)
    re=cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))
    cv2.imshow("checking",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)
    