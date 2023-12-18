from flask import Flask, request, Response
import numpy as np
import cv2
from resize_image import resize_img
import requests
import os


def get_watermark_image(filepath):
    try:
        addr = 'http://localhost:5000'
        test_url = addr + '/api/test'
        content_type = 'image/jpeg'
        headers = {'content-type': content_type}
        img = cv2.imread(filepath)
        _, img_encoded = cv2.imencode('.jpg', img)
        r = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
        r.raise_for_status()
        nparr = np.fromstring(r.content, np.uint8)
        im = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imwrite(filepath, im)
        return im
    except requests.exceptions.HTTPError as e:
        return e.response.status_code
    except requests.exceptions.ConnectionError:
        return "ConnectionError"
    except requests.exceptions.Timeout:
        return "TimeoutError"
    except requests.exceptions.RequestException:
        return "OtherError"


app = Flask(__name__)
app.debug = False


@app.route('/api/test', methods=['POST'])
def test():
    r = request
    nparr = np.fromstring(r.data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_resized = resize_img(img)

    filename = 'tmp.jpg'
    path = os.curdir + filename
    cv2.imwrite(path, img_resized)

    result = get_watermark_image(path)
    if isinstance(result, (int, str)):
        return Response(status=result)
    img2 = cv2.imread(path)
    _, img_encoded = cv2.imencode('.jpg', img2)
    return Response(img_encoded.tostring())


app.run(host="0.0.0.0", port=3000)
