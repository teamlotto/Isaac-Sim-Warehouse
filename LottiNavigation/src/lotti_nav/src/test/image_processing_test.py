import cv2
import os
import numpy as np

lower_white = np.array([9, 150, 40])
upper_white = np.array([20, 250, 70])

def mouse_callback(evnet, x, y, flags, param):
    global roi, lower_white, upper_white
    if evnet == cv2.EVENT_LBUTTONDOWN:
        color = roi[y, x]
        one_pixel = np.uint8([[color]])
        hsv = cv2.cvtColor(one_pixel, cv2.COLOR_BGR2HSV)
        print(hsv)

cv2.namedWindow('img_color')
cv2.setMouseCallback('img_color', mouse_callback)

root_dir = "/home/cj/isaac-sim-prj/git_clone/Isaac-Sim-Warehouse/job_in_docker/rolltainer/obj_train_data"
image_name = "1631776517550.png"

img_path = os.path.join(root_dir, image_name)
img = cv2.imread(img_path)

ymin, xmin = 470, 530
ymax, xmax = 530, 770
roi = img[ymin:ymax, xmin:xmax]
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv, lower_white, upper_white)
k = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, k)

cv2.imshow("img_color", roi)
cv2.imshow("hsv", mask)
cv2.imshow("opening", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()