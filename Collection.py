import cv2
import os
import uuid
import time
#Path for image folder
IMAGES_PATH='./images/collectedimages/'
#list of names
labels=["Hello","What","Your","Name",'Thank you', "My Friend", "ILoveYou"]
number_imgs=20

for label in labels:
    #create image folder
    out_dir = os.path.join(IMAGES_PATH,label)
    os.makedirs(out_dir)
    #open camera
    cap=cv2.VideoCapture(1)
    print('Collecting Images for {}'.format(label))
    time.sleep(10)
    #capture 20 frames
    for imgnum in range(number_imgs):
        
        ret , frame = cap.read()
        #assign unique id and save to image folder
        imgname=os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        
        if not cv2.imwrite(imgname, frame):
            raise IOError("Directory Doesn't exist")
            
        cv2.imshow('frame', frame)
        time.sleep(2)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()