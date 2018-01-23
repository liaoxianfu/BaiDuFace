from BaiDuFace.face_sdk_check import *

if __name__ == '__main__':
    uid = "unkonwn"
    user_info = "模特"
    group_id = "group2"

    client = init_set(app_id="你的app_Id", api_key="你的api_key",
                      secret_key="你的secret_key)

    image_list = [
        get_image_content('img/4.jpg'),
        get_image_content('img/5.jpg'),
    ]

    image = get_image_content('img/3.jpg')
    # for image in image_list:
    #     info = face_register(client=client, image=image, uid=uid, user_info=user_info, group_id=group_id)
    #     print(info)
    print(face_register(client, image=image, uid=uid, user_info=user_info, group_id=group_id))
    # print(face_update(client, image_list[0], uid, user_info, group_id))
    # print(face_delete(client, uid))

    print(get_group_list(client))
    print(get_user_info(client, uid))
    print(get_group_list(client))
    print(get_face_identify(client, image, group_id="group2"))
