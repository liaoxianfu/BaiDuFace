from BaiDuFace.json_byte_to_dict import json_byte_to_dict
from urllib import request


def get_token(api_key, secret_key):
    """
    动态获取获取token
    :param api_key:
    :param secret_key:
    :return: access_token
    """

    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + api_key \
           + '&client_secret=' + secret_key
    request_s = request.Request(host)
    request_s.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = request.urlopen(request_s)
    content = response.read()
    token_dict = json_byte_to_dict(content)

    access_token = token_dict.get('access_token')
    return access_token
