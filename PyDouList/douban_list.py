
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from pathlib import Path
import datetime
import re


doulist_page = 'https://www.douban.com/people/greatabel/doulists/all'

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
    regex = r'https://www.douban.com/doulist/.+(?=</a)'
    results = re.findall(regex, content)
    t = list(set(results))
    t.sort()
    counter = 0
    for item in t:
        counter += 1
        print(counter,'#:',item)
        print(item.split("/")[-2]+'   '+item.split(">")[-1])
    print('url count:', len(t))

def deal_with_doulist_url():
    # I ignore @@@ in .gitignore
    filename01 = '@@@01my_all_doulist#'+datetime.datetime.today().strftime('%Y-%m-%d')
    file01_path = Path("./" + filename01)
    content = ''
    if not file01_path.is_file():
        content = get_html(doulist_page)
        save_to_localfile(filename01, content)
    else:
        content = read_from_localfile(filename01)

    extract_doulist(content)

def main():
    deal_with_doulist_url()

if __name__ == "__main__":
    main()