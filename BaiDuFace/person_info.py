def get_personinfo(face_info_dict):
    """
    返回基本的识别信息
    :param face_info_dict:
    :return:
    """
    info_dict = {}
    result = face_info_dict.get('result')[0]
    age = result.get('age')
    info_dict['age'] = age
    info_dict['gender'] = result.get('gender')
    info_dict['gender_probability'] = result.get('gender_probability')
    return info_dict
