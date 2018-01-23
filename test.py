from BaiDuFace.get_access_token import get_token
from BaiDuFace.face_check import face_check
from BaiDuFace.person_info import get_personinfo
if __name__ == '__main__':
    API_KEY = '你的apikey'
    SECRET_KEY = '你的SECRET_KEY'
    token = get_token(API_KEY, SECRET_KEY)
    info = face_check(token, "img/3.jpg")
    result = info.get('result')[0]
    print(get_personinfo(info))
    print(info)
    print(result.get('beauty'))
