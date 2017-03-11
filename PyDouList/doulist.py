
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

doulist_page = 'https://www.douban.com/people/greatabel/doulists/all'

def get_html(url):
    try:
        request = Request(url, None, {"User-Agent": "Mozilla/5.0 AppleWebKit/537.36"})
        response = urlopen(request)
        data = response.read().decode('utf-8')
        print(data)
    except HTTPError as e:
        # do something
        print('Error code: ', e.code)
    except URLError as e:
        # do something
        print('Reason: ', e.reason)
    return data

def main():
    get_html(doulist_page)

if __name__ == "__main__":
    main()