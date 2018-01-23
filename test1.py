from BaiDuFace.face_sdk_check import init_set, get_image_content, get_face_info

if __name__ == '__main__':
    client = init_set(app_id="你的app_Id", api_key="你的api_key",
                      secret_key="你的secret_key")
    image_path = 'img/3.jpg'
    image = get_image_content(image_path)
    # 创建字典
    options = dict()
    options["max_face_num"] = 2
    options["face_fields"] = "age,beauty,gender,glasses"
    fae_info = get_face_info(client, image, options)
    print(fae_info)
