import cv2
from PIL import Image
import numpy as np

def resize_img(img_cv2):
    tmp_img = cv2.cvtColor(img_cv2, cv2.IMREAD_COLOR)
    img = Image.fromarray(tmp_img)
    width, height = img.size
    white_width = 0
    white_height = 0
    while (white_width < width or white_height < height):
        white_height += 9
        white_width += 16

    white_img = Image.new('RGB', (white_width, white_height), 'white')

    x = int((white_img.size[0] - width) / 2)
    y = int((white_img.size[1] - height) / 2)

    white_img.paste(img, (x, y))
    im_np = np.asarray(white_img)
    return im_np