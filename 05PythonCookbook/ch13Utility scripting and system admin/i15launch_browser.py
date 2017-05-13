import webbrowser

if __name__ == "__main__":
    url = "https://www.douban.com"
    result = webbrowser.open(url)
    webbrowser.open_new(url)
    print(result)
    c = webbrowser.get('firefox')
    c.open(url)
    