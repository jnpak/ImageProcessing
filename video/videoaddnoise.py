import glob
import cv2
import numpy as np


print("get images")

files = glob.glob('./images/*.jpg')

for i in range(len(files)):
    image = cv2.imread(files[i])
    row, col, ch = image.shape
    var = 0.1*10000
    sigma = var**0.5
    gauss = np.random.normal(0, sigma, (row, col, ch))
    noisy = image + gauss
    noisy = np.clip(noisy, 0, 255)
    noisy = noisy.astype('uint8')
    cv2.imwrite("./add/image%04d.jpg" % i, noisy)

print("add complete")