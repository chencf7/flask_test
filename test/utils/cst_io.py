# coding=utf-8
import os
from datetime import datetime
import requests
import base64

EXPORT_DIR = 'export'


def get_export_path():
    # os.path.dirname获取文件/文件夹的上级目录
    dir_path = os.path.dirname(os.path.abspath(__file__))
    super_dir_path = os.path.dirname(dir_path)
    export_dir_path = '{}\\{}'.format(super_dir_path, EXPORT_DIR)
    if not os.path.exists(export_dir_path):
        os.makedirs(export_dir_path)
    return export_dir_path
    # 获取项目执行的根目录
    # print(os.getcwd())


def write_str2txt(str_result, file_name, fp=None, file_encoding='utf-8'):
    export_path = get_export_path()
    tmp_d = datetime.now().strftime('%Y_%m_%d')
    tmp_t = datetime.now().strftime('%H%M%S_%f')
    if file_name == '' or file_name is None:
        file_name = '%s%s%s' % ('export', tmp_t, '.txt')

    file_path = None
    if fp is None:
        file_path = '{}\\{}'.format(export_path, tmp_d)
    else:
        file_path = '{}\\{}'.format(export_path, fp)

    fn = '{}\\{}'.format(file_path, file_name)
    if not os.path.exists(file_path):
        # print(file_path)
        # 创建路径
        os.mkdir(file_path)
        with open(fn, 'w', encoding=file_encoding) as f:
            f.write(str_result)
    else:
        with open(fn, 'a', encoding=file_encoding) as f:
            f.write(str_result)


def read_txt(filename, fp=None, file_encoding='utf-8'):
    export_path = get_export_path()
    try:
        with open(export_path+filename, 'r', encoding=file_encoding) as f:
            return f.read()
    except IOError as err:
        raise err


def download_image(data_link, image_type):
    try:
        export_path = get_export_path()
        file_name = None
        data = None
        if image_type == '.jpg':
            tmp = str(data_link).split('/')
            print(tmp[len(tmp)-1])
            file_name = export_path+'\\'+tmp[len(tmp)-1]+image_type
            response_img = requests.get(data_link)
            data = response_img.content
        elif image_type == 'base64':
            file_name = export_path+'\\'+'123.jpg'
            data = base64.b64decode(data_link)

        with open(file_name, 'wb') as f:
            f.write(data)
    except Exception as err:
        raise err
    pass
