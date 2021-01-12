import cv2
import numpy as np
import os

video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("PATH\\TO\\haarcascade_frontalface_alt.xml")
face_data = []
face_section = np.zeros((100,100),dtype='uint8')
dirpath = "PATH\\TO\\SAVE\\DATA_FOLDER"
skip = 0

cv2.namedWindow("Window")

while True:
    ret, frame = video_capture.read()
    if ret == False:
      continue
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame,1.3,5)
    faces = sorted(faces,key=lambda f:f[2]*f[3])
    for face in faces [-1:]:
      x, y, w, h = face
      cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
      face_section = frame[y - 10:y + h + 10, x - 10:x + w + 10]
      face_section = cv2.resize(face_section, (100, 100))
    cv2.imshow("Window", frame)
    cv2.imshow("Cropped",face_section)

    skip += 1
    if (skip % 10 == 0):
      face_data.append(face_section)
      print(len(face_data))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()

####################################################################################
##############      COMMENT ALL CODE BELOW FOR TRAINING THE MODEL     ##############
##############      COMMENT ALL CODE ABOVE FOR TESTING THE MODEL      ##############
####################################################################################

import cv2
import numpy as np
import os

face_data = np.array(face_data)
print(face_data.shape)
face_data = face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)

np.save(dirpath + "YOUR_NAME" + '.npy',face_data)
print("data successfully saved at " + dirpath+"YOUR_NAME"+'.npy')

def distance(v1, v2):
    # Eucledian
    return np.sqrt(((v1 - v2) ** 2).sum())

def knn(train, test, k=5):
    dist = []
    for i in range(train.shape[0]):
        ix = train[i, :-1]
        iy = train[i, -1]
        d = distance(test, ix)
        dist.append([d, iy])
    dk = sorted(dist, key=lambda x: x[0])[:k]
    labels = np.array(dk)[:, -1]
    output = np.unique(labels, return_counts=True)
    index = np.argmax(output[1])
    return output[0][index]

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("PATH\\TO\\haarcascade_frontalface_alt.xml")
skip = 0
dataset_path = 'PATH\\TO\\SAVE\\DATA_FOLDER'
face_data = []
labels = []
class_id = 0
names = {}

for fx in os.listdir(dataset_path):
    if fx.endswith('.npy'):
        names[class_id] = fx[:-4]
        print("Loaded " + fx)
        data_item = np.load(dataset_path + fx)
        face_data.append(data_item)
        target = class_id * np.ones((data_item.shape[0],))
        class_id += 1
        labels.append(target)
face_dataset = np.concatenate(face_data, axis=0)
face_labels = np.concatenate(labels, axis=0).reshape((-1, 1))
print(face_dataset.shape)
print(face_labels.shape)
trainset = np.concatenate((face_dataset, face_labels), axis=1)
print(trainset.shape)

while True:
    ret, frame = cap.read()
    if ret == False:
        continue
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    if (len(faces) == 0):
        continue
    for face in faces:
        x, y, w, h = face
        offset = 10
        face_section = frame[y - offset:y + h + offset, x - offset:x + w + offset]
        face_section = cv2.resize(face_section, (100, 100))
        out = knn(trainset, face_section.flatten())
        pred_name = names[int(out)]
        cv2.putText(frame, pred_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
    cv2.imshow("Faces", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()