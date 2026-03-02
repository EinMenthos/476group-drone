from djitellopy import tello
import cv2
from cvzone.FaceDetectionModule import FaceDetector
import time

def test():
    drone = tello.Tello()
    drone.connect()
    drone.streamoff()
    drone.streamon()
    detector = FaceDetector(minDetectionCon=0.5)
    #drone.takeoff()
    #drone.move_up(30)
    while True:
        img = drone.get_frame_read().frame
        img, bboxs = detector.findFaces(img, draw=False)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
        if(bboxs):
            #drone.move_up(30)
            print("up")
            time.sleep(5)
            #drone.move_down(30)
            print("down")
            time.sleep(5)
    #drone.land()
    cv2.destroyAllWindows()

test()
