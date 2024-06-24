from unicodedata import normalize
from urllib.parse import unquote_plus
from re import compile
from contextlib import suppress
import os
import argparse

# https://www.jianshu.com/p/fbe28e6415f3
Url_Path = compile(r'\%[0-9A-E]{2}')    # URL 乱码的正则表达式，形如 %E9
 
Codes = 'utf8', 'gbk', 'big5'           # 常见编码清单
 
 
def decode(data: bytes)->str:
    '''对二进制数据按指定的编码进行尝试解码后返回字符串，
    解码失败，则触发 UnicodeDecodeError 异常'''
    for code in Codes:
        with suppress(UnicodeDecodeError):
            return data.decode(code)     # 成功解码返回字符串
    raise UnicodeDecodeError             # 失败触发异常
 
 
def repare_name(name: str)->str:
    '''修改文件名乱码,
    返回正常的字符串'''
    if Url_Path.search(name):          # 判断文件名中是否有 URL 字符
        name = unquote_plus(name)      # 对 URL 文件名进行转码
    else:
        if os.name == 'posix':         # MacOS 系统中对重音字母进行压缩
            name = normalize('NFC', name)
        with suppress(UnicodeEncodeError):
            data = name.encode('latin1') # 将字符串转换成二进制，包含汉字的字符串会跳过
            name = decode(data)          # 对转换的二进制数据进行解码
    return name
 
def change_filename(under_this_path):
    # 修改某一个 文件夹下所有乱码的文件名
    from pathlib import Path
    for path in Path(under_this_path).glob('*.*'):
        new_name = repare_name(path.name)
        if path.name != new_name:
            print(path.name, '----> ', new_name)
            os.rename(under_this_path + '/' + path.name, 
                      under_this_path + '/' + new_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='absolute path of folder needed to process')
    parser.add_argument('--folder', type=str, default='/',
                        #use yolo3_darknet53_voc, yolo3_mobilenet1.0_voc, yolo3_mobilenet0.25_voc 
                        help="absolute path of folder needed to process")
    args = parser.parse_args()
    path_need_process = args.folder
    
    print(args.folder)
    for subdir, dirs, files in os.walk(path_need_process):
        for folder_name in dirs:
            new_fname = repare_name(folder_name)
            # print('new_fname=', new_fname)
            if folder_name != new_fname:
                print(folder_name, '#', new_fname)
                if os.path.isdir(path_need_process + '/' + folder_name):
                    os.rename(path_need_process + '/' + folder_name, 
                              path_need_process + '/' + new_fname)
                #处理子文件夹下文件
                change_filename(path_need_process + '/' + new_fname)

    change_filename(path_need_process)

