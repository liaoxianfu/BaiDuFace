import base64
from urllib import request
from urllib import parse
from BaiDuFace.json_byte_to_dict import json_byte_to_dict


def face_check(token, img_path):
    """
    人脸检测
    :param token:
    :param img_path:
    :return:
    """
    request_url = "https://aip.baidubce.com/rest/2.0/face/v1/detect"

    # 二进制方式打开图片文件
    f = open(img_path, 'rb')
    img = base64.b64encode(f.read())

    params = {"face_fields": "age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities", "image": img,
              "max_face_num": 5}
    # 注意encode要加encode(encoding='UTF8')
    # 不然会报错  POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.
    params = parse.urlencode(params).encode(encoding='UTF-8')

    access_token = token
    request_url = request_url + "?access_token=" + access_token

    request_s = request.Request(request_url, params)

    request_s.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = request.urlopen(request_s)
    content = response.read()
    face_info_dict = json_byte_to_dict(content)
    return face_info_dict
