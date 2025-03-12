import cv2
import mediapipe as mp
import winsound
import time

camera = cv2.VideoCapture(0)
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
x1 = y1 = x2 = y2 = 0

while True:
    success, image = camera.read()
    image = cv2.flip(image,1)
    fh , fw , _ = image.shape
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_image)
    landmark_points = output.multi_face_landmarks
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks):
            x = int(landmark.x * fw) 
            y = int(landmark.y * fh)
            if id == 43:
                x1 = x
                y1 = y
            if id == 287:
                x2 = x
                y2 = y
                dist = int(((x2-x1)**2 + (y2-y1)**2) ** (0.5))
                print(dist)
                if dist > 80:
                    cv2.imwrite("selfie.png",image)
                    winsound.PlaySound("ssSound.wav", winsound.SND_FILENAME)
                    time.sleep(1)
    cv2.imshow("AUTO CAPTURE SMILING FACE", image)
    key = cv2.waitKey(100) 
    if key == 27:
       break
camera.release()
cv2.destroyAllWindows() 