from BaiDuFace.face_sdk_check import get_face_compare, init_set, get_image_content

if __name__ == '__main__':
    image_list = [

        get_image_content('img/4.jpg'),

        get_image_content('img/5.jpg'),
        # get_image_content('img/3.jpg')
    ]
    client = init_set(app_id="你的app_Id", api_key="你的api_key",
                      secret_key="你的secret_key)

    """ 如果有可选参数 """
    options = dict()
    options["ext_fields"] = "qualities"
    options["image_liveness"] = ",faceliveness"
    options["types"] = "7,13"
    face_info = get_face_compare(client=client, image_list=image_list, options=options)
    print(face_info)
