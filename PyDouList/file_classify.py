import os
from difflib import SequenceMatcher
import zhconv
import myconfig
from file_transform import file_transform
def similar(a, b):
    if a == b :
        return 1
    if (a in b) or (b in a):
        # 加上这个可能出错，需要检查
        return 0.777
    return SequenceMatcher(None, a, b).ratio()

def get_files(file_wait_to_process_directory):
    count = 0
    file_dic = {}
    #  遍历所有文件，文件夹
    for fpathe,dirs,fs in os.walk(file_wait_to_process_directory):
      for f in fs:
        filename, file_ext = os.path.splitext(f)
        if file_ext in myconfig.white_extension_name:
            count += 1
            # print(count, filename, '#',file_ext,'#',os.path.join(fpathe,f))
            file_dic[filename] = os.path.join(fpathe,f)
    print('local file count=', count)
    return file_dic


def remove_str_part(istr,start_mark, end_mark):
    start = istr.find(start_mark)
    end = istr.find(end_mark)
    if start != -1 and end != -1:
        remove_part = istr[start:end+1]
        istr = istr.replace(remove_part,'')
    return istr

def format_str_for_compare(istr):
    istr = remove_str_part(istr, '(', ')')
    istr = remove_str_part(istr, '（', '）')
    for ch in ['”', '“', '《','》']:
        istr = istr.replace(ch,'')
    for ch in ['.','·','：',":","'"]:
        istr = istr.replace(ch, ' ')
    istr = istr.replace('Ⅱ','II')
    istr = istr.lower()
    # https://pypi.python.org/pypi/zhconv 繁体转换简体
    istr = zhconv.convert(istr, 'zh-cn')
    return istr

def classify_handler(detailDic):
    counter = 0
    dou_counter = 0
    file_dic = get_files(myconfig.file_wait_to_process_directory)
    for key, single_doulist in detailDic.items():
        print('\n' + key + '\n')

        for book in single_doulist:
            dou_counter += 1
            similarity = 0
            filenameA = ''
            filepathA = ''
            for filename, filepath in file_dic.items():
                temp_similarity = similar(format_str_for_compare(book.name), format_str_for_compare(filename))
                if temp_similarity > similarity:
                    similarity = temp_similarity
                    filenameA = filename
                    filepathA = filepath
                    
                    # print(similarity, 'counter=', counter,
                    #     'douban name=', book.name, '#'*5,'filename=', filename)
            if similarity > 0.61:
                counter += 1
                # print(similarity,'counter=', counter, book.name,'#',filenameA,book.been_read_date )

                file_transform(filepathA, myconfig.file_wait_to_process_directory, 
                    myconfig.file_outupt_directory, key.rsplit('/', 1)[1].replace('@@@02',''))

                # if similarity < 0.7 and similarity != 0.666:
            else:
                print(similarity,'failed counter=', counter, book.name,'#',filenameA,book.been_read_date )
    print('counter=', counter,'dou_counter=', dou_counter)
            # elif book.been_read_date > '2016-06-01':
            #     print('>'*5, ' miss find:', book.name,format_str_for_compare(book.name), book.been_read_date)


            # book.displayDoubanBook()

