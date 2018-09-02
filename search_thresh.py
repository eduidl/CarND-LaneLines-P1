import cv2
import os

def nothing(x):
    pass

IMG_DIR = "test_images/"
files = os.listdir(IMG_DIR)
srcs = [cv2.imread("{}{}".format(IMG_DIR, file_)) for file_ in files]
grays = [cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) for src in srcs]

cv2.namedWindow('setting', cv2.WINDOW_NORMAL)
cv2.createTrackbar('min', 'setting',   0, 255, nothing)
cv2.createTrackbar('max', 'setting', 255, 255, nothing)

while(True):
    k = cv2.waitKey(1)
    if k == 27:
        break;
    min_ = cv2.getTrackbarPos('min', 'setting')
    max_ = cv2.getTrackbarPos('max', 'setting')

    results = [cv2.inRange(gray, min_, max_) for gray in grays]

    row1 = cv2.hconcat([results[0], results[1]])
    row2 = cv2.hconcat([results[2], results[3]])
    row3 = cv2.hconcat([results[4], results[5]])

    cv2.imshow('setting', cv2.vconcat([row1, row2, row3]))

cv2.destroyAllWindows()
