import cv2


import cvlib as cv

from cvlib.object_detection import draw_bbox

import matplotlib.pyplot as plt


im = cv2.imread('test.jpg')


bbox, label, conf = cv.detect_common_objects(im)


output_image = draw_bbox(im, bbox, label, conf)






numberofcars = label.count('car')


print('Number of cars in the image is ' + str(numberofcars))




## show by matplotlib
# plt.imshow(output_image)
# plt.show()


while True:
    cv2.imshow("test image", output_image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break