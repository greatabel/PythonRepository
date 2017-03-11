
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from pathlib import Path
import datetime


doulist_page = 'https://www.douban.com/people/greatabel/doulists/all'

def get_html(url):
    try:
        request = Request(url, None, {"User-Agent": "Mozilla/5.0 AppleWebKit/537.36"})
        response = urlopen(request)
        data = response.read().decode('utf-8')
        print('len(data)=',len(data))
    except HTTPError as e:
        # do something
        print('Error code: ', e.code)
    except URLError as e:
        # do something
        print('Reason: ', e.reason)
    return data

def save_to_localfile(filename, content):
    with open(filename, 'wt') as f:
        f.write(content)

def main():
    filename01 = '@@@01my_all_doulist#'+datetime.datetime.today().strftime('%Y-%m-%d')
    file01 = Path("./" + filename01)
    if not file01.is_file():
        content = get_html(doulist_page)
        save_to_localfile(filename01, content)


if __name__ == "__main__":
    main()