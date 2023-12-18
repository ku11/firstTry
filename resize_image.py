import cv2
from PIL import Image
import numpy as np

def resize_img(img_cv2):
    tmp_img = cv2.cvtColor(img_cv2, cv2.IMREAD_COLOR)
    img = Image.fromarray(tmp_img)
    width, height = img.size
