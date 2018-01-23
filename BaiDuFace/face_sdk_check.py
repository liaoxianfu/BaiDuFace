from aip import AipFace


def init_set(app_id, api_key, secret_key):
    """
    app_id在百度云控制台中创建，常量api_key与secret_key是在创建完毕应用后，
    系统分配给用户的，均为字符串，用于标识用户，为访问做签名验证，可在AI服务控制台中的应用列表中查看。
    注意：如您以前是百度云的老用户，其中api_key对应百度云的“Access Key ID”，secret_key对应百度云的“Access Key Secret”。
    :param app_id:
    :param api_key:
    :param secret_key:
    :return: client
    """

    client = AipFace(app_id, api_key, secret_key)
    return client


def get_image_content(file_path):
    """
    读取图片\n
    :param file_path:图片路径\n
    :return:image:base64格式的图片数据\n
    """
    with open(file_path, 'rb') as fp:
        image = fp.read()
        return image


def get_face_info(client, image, options=None):
    """
    获取带附加参数的信息
    :param client:
    :param image:
    :param options:默认为None
    :return:face_info
    """
    face_info = client.detect(image, options)
    return face_info


def get_face_compare(client, image_list, options=None):
    """
    调用一组image_lsit 附加参数 比较list中用户的人脸相似度
    :param client:
    :param image_list:
    :param options:默认为None
    :return:compare_info
    """

    compare_info = client.match(image_list, options)
    return compare_info


def face_register(client, image, uid, user_info, group_id, options=None):
    """
    人脸注册
    如果需要将一个uid注册到多个group下，group_id需要用多个逗号分隔，
    每个group_id长度限制为48个英文字符。注：group无需单独创建，
    注册用户时则会自动创建group。
    :param client:
    :param image:
    :param uid:
    :param user_info:
    :param group_id:
    :param options:
    :return: info
    """
    info = client.addUser(uid, user_info, group_id, image, options)

    return info


def face_update(client, image, uid, user_info, group_id, options=None):
    """
    针对一个uid执行更新操作，新上传的人脸图像将覆盖此uid原有所有图像。
    如果options中添加了action_type:replace,则不会报错，
    并自动注册该uid，操作结果等同注册新用户。
    :param client:
    :param image:
    :param uid:
    :param user_info:
    :param group_id:
    :param options:
    :return:info
    """
    info = client.updateUser(uid, user_info, group_id, image, options)
    return info


def face_delete(client, uid, options=None):
    """
    用于从人脸库中删除一个用户。

    人脸删除注意事项：

        删除的内容，包括用户所有图像和身份信息；
        如果一个uid存在于多个用户组内，将会同时将从各个组中把用户删除
        如果指定了group_id，则只删除此group下的uid相关信息

    :param client:
    :param uid:
    :param options:
    :return:info
    """
    info = client.deleteUser(uid, options)
    return info


def get_user_info(client, uid, options=None):
    """
    用户组信息的查询
    用于查询人脸库中某用户的详细信息。
    :param client:
    :param uid:
    :param options:
    :return:
    """
    user_info = client.getUser(uid, options)
    return user_info


def get_group_list(client, options=None):
    """
    用于查询用户组的列表。
    :param client:
    :param options:{'start':xx,'end':xx}
    :return:
    """
    group_list_info = client.getGroupList(options)

    return group_list_info


def get_group_user_info(client, group_id, options=None):
    """
    用于查询指定用户组中的用户列表。
    :param client:
    :param group_id:
    :param options:
    :return:
    """
    group_user_info = client.getGroupUsers(group_id, options)

    return group_user_info


def get_face_identify(client, image, group_id, options=None):
    """
    用于计算指定组内用户，与上传图像中人脸的相似度。识别前提为您已经创建了一个人脸库。

    典型应用场景：如人脸闸机，考勤签到，安防监控等。
    :param client:
    :param image:
    :param group_id:
    :param options:
    :return:
    """
    identify_result = client.identifyUser(group_id, image, options)
    return identify_result


def get_face_multi_identify(client, image, group_id, options=None):
    """
    待识别的图片中，存在多张人脸的情况下，支持在一个人脸库中，一次请求，
    同时返回图片中所有人脸的识别结果。
    :param client:
    :param image:
    :param group_id:
    :param options:
    :return:
    """
    face_info = client.multiIdentify(group_id, image, options)
    return face_info
