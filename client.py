from __future__ import print_function
import cv2


def save_image(image):
    filename = 'Processed image.png'
    cv2.imwrite(filename, image)




