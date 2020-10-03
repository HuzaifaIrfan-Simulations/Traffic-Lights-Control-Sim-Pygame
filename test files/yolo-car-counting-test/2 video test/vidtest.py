import cv2


import matplotlib.pyplot as plt
from cvlib.object_detection import draw_bbox

import cvlib as cv




cap=cv2.VideoCapture("video.mp4")



while True:
    success, img = cap.read()

    bbox, label, conf = cv.detect_common_objects(img)

    # cv2.imshow("test video", img)

    output_image = draw_bbox(img, bbox, label, conf)

    cv2.imshow("test video", output_image)
    
    # plt.imshow(output_image)
    # plt.show()

    numberofcars = label.count('car')


    print('Number of cars in the image is ' + str(numberofcars))


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break




# im = cv2.imread('test.jpg')


# bbox, label, conf = cv.detect_common_objects(im)


# output_image = draw_bbox(im, bbox, label, conf)
# plt.imshow(output_image)
# plt.show()





numberofcars = label.count('car')


print('Number of cars in the image is ' + str(numberofcars))
