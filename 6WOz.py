import cv2
import dropbox
import time
import random
import pythonos
import shutil
start_time = time.time()
def takeSnapshot():
    number = random.randint(0, 100)
    #Initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while (result):
        #Read the frames while the camera is on
        ret, frame = videoCaptureObject.read()
        #cv2.imwrite() is used to save an image to any storage device.
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        start_time - time.time
        result = False
    return img_name
    print("snapshot taken")
    #releases the camera
    videoCaptureObject.release()
    #Close all the windows that might be open
    cv2.destroyAllWindows()
    def FileUploadImages