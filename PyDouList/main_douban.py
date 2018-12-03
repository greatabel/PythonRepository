from pathlib import Path
import re
import os

from  detail_doulist import single_doulist_save_html, deal_with_folder_all_htmls
import myconfig
from common import persistent_list_to_local, read_persistentedlist_from_local, get_html,\
                   save_to_localfile,read_from_localfile
from file_classify import classify_handler
from record_generator import record_generator


def extract_doulist(content):
    # regex = r'https://www.douban.com/doulist/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+</a>'
    # http://stackoverflow.com/questions/18129041/python-regex-search-for-string-which-starts-and-ends-with-the-given-text
    dic = {}
    regex = r'' + myconfig.doulist_prex + '.+(?=</a)'
    results = re.findall(regex, content)
    t = list(set(results))
    t.sort()
    counter = 0
    for item in t:
        counter += 1
        # print(counter,'#:',item)
        # 排除网络日志，只处理 书单豆列
        print(item.split("/")[-2]+'   '+item.split(">")[-1])
        if (item.split(">")[-1] not in myconfig.blacklist ) and ("网记" not in item.split(">")[-1]):
            dic[item.split(">")[-1]] = myconfig.doulist_prex + item.split("/")[-2]
    print('url count:', len(t))
    return dic


def deal_with_doulist_url():
    pickle01_path = Path(myconfig.filename01 + '.mypickle')
    if not pickle01_path.is_file():
        file01_path = Path(myconfig.filename01)
        content = ''
        if not file01_path.is_file():
            for i in range(0,myconfig.scrawler_pagelimit_doulist):
                content += get_html(myconfig.doulist_page + '?start=' + str(20 * i))
            save_to_localfile(myconfig.filename01, content)
        else:
            content = read_from_localfile(myconfig.filename01)
        persistent_list_to_local(myconfig.filename01 + '.mypickle', extract_doulist(content))
    return read_persistentedlist_from_local(myconfig.filename01 + '.mypickle')


def main():
    doulist_list = deal_with_doulist_url()
    
    if not os.path.exists(myconfig.directory):
        os.makedirs(myconfig.directory)
        for doulistname, single_doulist in doulist_list.items():
            single_doulist_save_html(doulistname, single_doulist, 
                                     myconfig.directory, myconfig.scrawler_pagelimit)

    pickle02_path = Path( myconfig.directory + "/" + myconfig.filename02 + '.mypickle')
    if not pickle02_path.is_file():
        deal_with_folder_all_htmls(myconfig.directory)
    detailDic = read_persistentedlist_from_local(myconfig.filename02 + '.mypickle', myconfig.directory)
    classify_handler(detailDic)
    record_generator()


if __name__ == "__main__":
    main()
