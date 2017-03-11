import pickle
import pprint
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def save_to_localfile(filename, content):
    with open(filename, 'wt') as f:
        f.write(content)


def read_from_localfile(filename):
    with open(filename, "r") as myfile:
        content = myfile.read()
    return content


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

def get_html(url):
    try:
        request = Request(url, None, {"User-Agent": "Mozilla/5.0 AppleWebKit/537.36"})
        response = urlopen(request)
        data = response.read().decode('utf-8')
        print('len(data)=', len(data))
    except HTTPError as e:
        print('Error code: ', e.code)
    except URLError as e:
        print('Reason: ', e.reason)
    return data