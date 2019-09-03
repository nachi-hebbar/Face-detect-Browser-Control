
import cv2
import os
import webbrowser
import time


gmail="https://mail.google.com/mail/u/0/#inbox"
youtube="https://www.youtube.com/channel/UCJPihOKkiT7TqP7NK9-GtuQ?view_as=subscriber"
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
  
# capture frames from a camera 
def check_face():
    cap = cv2.VideoCapture(0) 
  
# loop runs if capturing has been initialized. 
    while 1:  
  
    # reads frames from a camera 
        ret, img = cap.read()  
  
    # convert to gray scale of each frames 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
    # Detects faces of different sizes in the input image 
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        print("No of faces found:",len(faces)
    
        if len(faces)>0:
            a=input("Do you want to open youtube or gmail?")
            if a=='g':
                webbrowser.open_new(gmail)
            else:
                webbrowser.open_new(youtube)
            break
        else:
            shutdown=input("You want to shut down")
            if shutdown=='y':
                os.system('shutdown -s')
            else:
                print('Shutdown Aborted')
            break


    # Wait for Esc key to stop 
  
# Close the window 
    cap.release() 
  
# De-allocate any associated memory usage 
    cv2.destroyAllWindows()

check_face()
time.sleep(15)
check_face()







    
