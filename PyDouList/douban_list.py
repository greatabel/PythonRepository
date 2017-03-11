
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from pathlib import Path
import datetime
import re
import pickle
import pprint


doulist_page = 'https://www.douban.com/people/greatabel/doulists/all'
doulist_prex = 'https://www.douban.com/doulist/'
# filename01 = '@@@01my_all_doulist#'+datetime.datetime.today().strftime('%Y-%m-%d')
filename01 = '@@@01my_all_doulist#'
blacklist = ['Fashion-Old', 'abel的日记','magzine']

def get_html(url):
    try:
        request = Request(url, None, {"User-Agent": "Mozilla/5.0 AppleWebKit/537.36"})
        response = urlopen(request)
        data = response.read().decode('utf-8')
        print('len(data)=',len(data))
    except HTTPError as e:
        print('Error code: ', e.code)
    except URLError as e:
        print('Reason: ', e.reason)
    return data

def save_to_localfile(filename, content):
    with open(filename, 'wt') as f:
        f.write(content)

def read_from_localfile(filename):
    with open (filename, "r") as myfile:
        content = myfile.read()
    return content

def extract_doulist(content):
    # regex = r'https://www.douban.com/doulist/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+</a>'
    # http://stackoverflow.com/questions/18129041/python-regex-search-for-string-which-starts-and-ends-with-the-given-text
    dic = {}
    regex = r''+ doulist_prex + '.+(?=</a)'
    results = re.findall(regex, content)
    t = list(set(results))
    t.sort()
    counter = 0
    for item in t:
        counter += 1
        # print(counter,'#:',item)
        print(item.split("/")[-2]+'   '+item.split(">")[-1])
        if item.split(">")[-1] not in blacklist:
            dic[item.split(">")[-1]] = doulist_prex + item.split("/")[-2]
    print('url count:', len(t))
    print(dic)
    return dic

def persistent_list_to_local(filename, dic):
    # http://www.cnblogs.com/pzxbc/archive/2012/03/18/2404715.html
    output = open(filename, 'wb')
    pickle.dump(dic, output)
    output.close()

def read_persistentedlist_from_local(filename):
    pkl_file = open(filename, 'rb')
    data = pickle.load(pkl_file)
    pprint.pprint(data)
    return data

def deal_with_doulist_url():
    # I ignore @@@ in .gitignore
    file01_path = Path("./" + filename01)
    content = ''
    if not file01_path.is_file():
        content = get_html(doulist_page)
        save_to_localfile(filename01, content)
    else:
        content = read_from_localfile(filename01)

    pickle01_path = Path("./" + filename01 + '.mypickle')
    if not pickle01_path.is_file():
        persistent_list_to_local(filename01 + '.mypickle',extract_doulist(content))
    read_persistentedlist_from_local(filename01 + '.mypickle')

def main():
    deal_with_doulist_url()

if __name__ == "__main__":
    main()