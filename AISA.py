from ultralytics import YOLO
import cv2
from time import sleep
from Audio import TTS
def main():
    Predictions()
    #Training()

def Training():
    #Loading pre-trained model on object detection
    model = YOLO("yolo11n-cls.pt")
    #training object detection model on sign language gestures
    model.train(data="./images", epochs=100, batch=2, imgsz=640, device=0, workers=8, pretrained=True, val=True, plots=True, save=True, show=True, optimize=True, lr0=0.001, lrf=0.01, fliplr=0.0, amp=False)

def Predictions():
    
    model = YOLO("./runs/classify/train8/weights/last.pt")
    
    cap = cv2.VideoCapture(1)
    
    while cap.isOpened():

        # Read feed
        ret, frame = cap.read()
        results = model.predict(frame)
        
        #Storing result names
        names_dict = results[0].names
        
        #returning single highest probability
        probs = results[0].probs.top1 
        
        #matches name to single highest probability
        names = names_dict[probs]

        #speaks the name
        TTS(names)

        #breaking 'not' bad
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()