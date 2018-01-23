from BaiDuFace.face_sdk_check import *

if __name__ == '__main__':
    client = init_set(app_id="ÄãµÄapp_Id", api_key="ÄãµÄapi_key",
                      secret_key="ÄãµÄsecret_key)
    options = dict()
    options["ext_fields"] = "faceliveness"
    options["detect_top_num"] = 3
    options["user_top_num"] = 2
    group_id = 'group1,group2'
    image = get_image_content('img/4.jpg')
    info = get_face_multi_identify(client, image, group_id, options=options)
    print(info)
