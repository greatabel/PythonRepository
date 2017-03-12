from time import sleep
import glob
import os
from bs4 import BeautifulSoup

from common import persistent_list_to_local, read_persistentedlist_from_local, get_html,\
                   save_to_localfile, read_from_localfile
import myconfig
from book import DoubanBook

def single_doulist_save_html(name, url, directory, scrawler_pagelimit=3):
    print('in single_doulist_handle:',name, url)
    index = 0
    for i in range(0,scrawler_pagelimit):
        print(url + '/?start=' + str(index) + '&sort=time&sub_type=')
        content = get_html(url + '/?start=' + str(index) + '&sort=time&sub_type=')
        save_to_localfile('@@@02' + name + '#page' + str(i), content, directory)
        index += 25
        sleep(1)

def single_page(content):
    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find_all("div", "doulist-item")
    books = []
    for item in items:
        # get book name
        bookName = ''
        content = item.find("div", "title")
        if content != None:
            href = content.find("a")
            if href != None and href.string != None:
                bookName = href.string.strip()
        # get book author
        # http://stackoverflow.com/questions/5275359/using-beautifulsoup-to-extract-text-between-line-breaks-e-g-br-tags
        bookAuthor = ''
        bookPubDate = ''
        content = item.find("div", "abstract")
        for a in content.childGenerator(): 
            # print(type(a), str(a))
            if("作者:" in str(a)):
                bookAuthor = str(a).strip()[3:].strip()
                # print('#'*3,str(a).lstrip()[3:].strip(),'#'*3)
            if("出版年:" in str(a)):
                bookPubDate = str(a).strip()[4:].strip()
                # print('@'*3,str(a).lstrip()[4:].strip(),'@'*3)

        been_read_date = ''
        content = item.find("div", "actions")

        if content != None:
            span = content.time.find("span")
            # print('span:',span, span.attrs['title'])
            if span != None and span.attrs['title'] != None:
                been_read_date = span.attrs['title'].strip()

        book = DoubanBook(bookName, bookAuthor, bookPubDate, been_read_date)
        # book.displayDoubanBook()
        books.append(book)
    return books

def deal_with_folder_all_htmls(directory):
    print(directory)
    filelist = glob.glob( directory + "/*")
    filelist.sort()
    counter = 0
    dic = {}
    for item in filelist:
        # item = item.split("/")[-1]
        counter += 1
        print(counter,item)
        content = read_from_localfile(item)
        books = single_page(content)
        start = item.index('#')
        item = item[:start]
        # 合并多页
        if item in dic:
            # print(item ,' already exist')
            dic[item] = dic[item] + books
        else:
            dic[item] = books
    persistent_list_to_local(myconfig.filename02 + '.mypickle', dic, directory)


