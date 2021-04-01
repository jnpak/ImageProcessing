__author__ = 'Seran'

import cv2


# 영상의 의미지를 연속적으로 캡쳐할 수 있게 하는 class
vidcap = cv2.VideoCapture('video.mp4')

count = 1

while (vidcap.isOpened()):
    ret, image = vidcap.read()

    if not ret:
        break

    cv2.imwrite("./images/frame%04d.jpg" % count, image)

    print('Saved frame%d.jpg' % count)
    count += 1

vidcap.release()
