import cv2

img = cv2.imread("D:\Downloads\doggo.jpg")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("D:\Downloads\Default.jpg", img)

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def viewImage(img, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Syntax for cropping <image_name>[y:y+h, x:x+w]
crop = rgb_img[50:700, 100:900]
viewImage(crop, "Cropped Image")
cv2.imwrite("D:\Downloads\Cropped.jpg", crop)

# Provide the % times of the original image you want to scale
scaling = 20
#Change Width and Height
width = int(rgb_img.shape[1] * scaling / 100)
height = int(rgb_img.shape[0] * scaling / 100)
dim = (width,height)
resized = cv2.resize(img,dim, interpolation = cv2.INTER_AREA)
viewImage(resized, "Resized Image by 20%")
cv2.imwrite("D:\Downloads\Resized.jpg", resized)

(h, w, d) = rgb_img.shape
center_img = (w//2, h//2)
rotationMatrix = cv2.getRotationMatrix2D(center_img, 180, 1.0)
rotated = cv2.warpAffine(rgb_img, rotationMatrix, (w, h))
viewImage(rotated, "Rotated Image 180 degrees")
cv2.imwrite("D:\Downloads\Rotated.jpg", rotated)

gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
ret, threshold_img = cv2.threshold(gray_img,127,255,0)
viewImage(gray_img, "Grayscale Image")
cv2.imwrite("D:\Downloads\Gray.jpg", gray_img)
viewImage(threshold_img, "Threshold Image")
cv2.imwrite("D:\Downloads\Thresh.jpg", threshold_img)

blurred = cv2.GaussianBlur(rgb_img, (61,61), 0)
viewImage(blurred, "Blurred Image")
cv2.imwrite("D:\Downloads\Blur.jpg", blurred)

output = rgb_img.copy()
cv2.rectangle(output, (600,200), (900, 550), (0, 255, 255), 10)
viewImage(output, "Rectangle on an Image")
cv2.imwrite("D:\Downloads\Rect.jpg", output)

import os
cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
haar_model = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml')

image_path1 = "D:\Downloads\Face1.jpg"
image_path2 = "D:\Downloads\Face2.jpg"
face_cascade = cv2.CascadeClassifier(haar_model)

image1 = cv2.imread(image_path1)
image2 = cv2.imread(image_path2)
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
faces1 = face_cascade.detectMultiScale(gray1, scaleFactor = 1.1,minNeighbors = 5, minSize = (10,10))
faces2 = face_cascade.detectMultiScale(gray2, scaleFactor = 1.1,minNeighbors = 5, minSize = (10,10))
face_detected = format(len(faces1)) + "Face detected!"
face_detected = format(len(faces2)) + "Face detected!"
print(face_detected)
for(x, y, w, h) in faces1:
    cv2.rectangle(image1, (x, y), (x + w, y + h), (255, 255, 0), 2)
viewImage(image1, face_detected)
cv2.imwrite("D:\Downloads\FaceDetect1.jpg", image1)
for(x, y, w, h) in faces2:
    cv2.rectangle(image2, (x, y), (x + w, y + h), (255, 255, 0), 2)
viewImage(image2, face_detected)
cv2.imwrite("D:\Downloads\FaceDetect2.jpg", image2)
