import os
import myconfig


def get_files(file_wait_to_process_directory, file_outupt_directory):
    count = 0
    file_dic = {}
    #  遍历所有文件，文件夹
    for fpathe,dirs,fs in os.walk(file_wait_to_process_directory):
      for f in fs:
        filename, file_ext = os.path.splitext(f)
        if file_ext in myconfig.white_extension_name:
            count += 1
            print(count, filename, '#',file_ext,'#',os.path.join(fpathe,f))
            file_dic[filename] = os.path.join(fpathe,f)
    return file_dic


def classify_handler(detailDic):
    for key, single_doulist in detailDic.items():
        print('\n' + key + '\n')
        for book in single_doulist:
            book.displayDoubanBook()
    get_files(myconfig.file_wait_to_process_directory, myconfig.file_outupt_directory)
