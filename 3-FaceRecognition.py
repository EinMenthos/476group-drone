from djitellopy import Tello
import cv2
from cvzone.FaceDetectionModule import FaceDetector

#enable venv
#source source myenv/bin/activate 

# Traceback (most recent call last):
#  File "<string>", line 1, in <module>
#    import mediapipe as mp; print(mp.__version__); print(hasattr(mp,'solutions')); print(mp.solutions.face_detection)

# brew install python@3.11
# python3.11 -m venv .venv311
# source .venv311/bin/activate
# pip install --upgrade pip

#by using those two commands, found that current mediapipe version dropped solution.
# python -c "import mediapipe as mp; print(mp.__version__); print(hasattr(mp,'solutions'))"
# python -c "import mediapipe, os; print(os.listdir(os.path.dirname(mediapipe.__file__)))"

# Finally found that mediapipe is wrong version.

# pip install djitellopy opencv-python cvzone "mediapipe==0.10.21"
# or
# pip install -r requirements.txt
# python -c "import mediapipe as mp; print(mp.__version__); print(hasattr(mp,'solutions')); print(mp.solutions.face_detection)"
# return TRUE!!!

me = Tello()
me.connect()
print("Test: Battery Status: ")

print(me.get_battery())
me.streamoff()
me.streamon()

detector = FaceDetector()
while True:
    img = me.get_frame_read().frame
    img, bboxs = detector.findFaces(img, draw = True)
    cv2.imshow("Image", img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
me.end()