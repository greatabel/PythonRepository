
from pathlib import Path
import datetime # NOQA
import re
import os

from  single_doulist import single_doulist_handle
import myconfig
from common import persistent_list_to_local, read_persistentedlist_from_local, get_html,\
                   save_to_localfile,read_from_localfile


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
        print(item.split("/")[-2]+'   '+item.split(">")[-1])
        if item.split(">")[-1] not in myconfig.blacklist:
            dic[item.split(">")[-1]] = myconfig.doulist_prex + item.split("/")[-2]
    print('url count:', len(t))
    print(dic)
    return dic


def deal_with_doulist_url():
    pickle01_path = Path("./" + myconfig.filename01 + '.mypickle')
    if not pickle01_path.is_file():
        file01_path = Path("./" + myconfig.filename01)
        content = ''
        if not file01_path.is_file():
            content = get_html(myconfig.doulist_page)
            save_to_localfile(myconfig.filename01, content)
        else:
            content = read_from_localfile(myconfig.filename01)
        persistent_list_to_local(myconfig.filename01 + '.mypickle', extract_doulist(content))
    return read_persistentedlist_from_local(myconfig.filename01 + '.mypickle')


def main():
    doulist_list = deal_with_doulist_url()
    directory = datetime.datetime.today().strftime('%Y-%m-%d')
    if not os.path.exists(directory):
        os.makedirs(directory)
    for doulistname, doulist in doulist_list.items():
        single_doulist_handle(doulistname, doulist, directory)


if __name__ == "__main__":
    main()
