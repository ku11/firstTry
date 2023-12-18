from __future__ import print_function
import requests
import numpy as np
import cv2


def save_image(image):
    filename = 'Processed image.png'
    #print(f"filename, image: {filename}, {image}")
    cv2.imwrite(filename, image)


def get_watermark_image(imagename):
    try:
        addr = 'http://localhost:3000'
        test_url = addr + '/api/test'
        content_type = 'image/jpg'
        headers = {'content-type': content_type}

        print(f"imagename: {imagename}")
        img = cv2.imread(imagename)
        _, img_encoded = cv2.imencode('.jpg', img)

        r = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
        r.raise_for_status()
        nparr = np.fromstring(r.content, np.uint8)
        im = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return im

    except requests.exceptions.HTTPError:
        raise Exception("Http Error")
    except requests.exceptions.ConnectionError:
        raise Exception("Connecting Error")
    except requests.exceptions.Timeout:
        raise Exception("Timeout Error")
    except requests.exceptions.RequestException:
        raise Exception("OOps: Something Else")


