from time import sleep
import glob
import os
from bs4 import BeautifulSoup

from common import persistent_list_to_local, get_html,\
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
            # print(content.time.string)
            # span = content.time.find("span")
            # # print('span:',span, span.attrs['title'])
            # if span != None and span.attrs['title'] != None:
            #     been_read_date = span.attrs['title'].strip()
            if content.time.string is not None:
                been_read_date = content.time.string

        book = DoubanBook(bookName, bookAuthor, bookPubDate, been_read_date)
        # book.displayDoubanBook()
        if book.been_read_date > myconfig.last_async_time:
            books.append(book)
    return books

def circulate_readen_order(dic_for_sort_readen_order, detailDic):
    # https://edumaven.com/python-programming/sort-dictionary-by-value
    sorted_names = sorted(dic_for_sort_readen_order, key=dic_for_sort_readen_order.__getitem__)
    # sorted_names = sorted(dic_for_sort_readen_order, key=dic_for_sort_readen_order.__getitem__, reverse=True)
    read_order = 0
    dic_name_order = {}
    for k in sorted_names:
        dic_name_order[k] = read_order 
        read_order += 1
    for key, single_doulist in detailDic.items():
        for idx, book in enumerate(single_doulist):
            if book._name in dic_name_order:
                single_doulist[idx].set_readen_order(dic_name_order[book._name])
                single_doulist[idx].set_category(key.rsplit('/', 1)[1].replace('@@@02',''))

                # single_doulist[idx].displayDoubanBook()


def deal_with_folder_all_htmls(directory):
    filelist = glob.glob( directory + "/*")
    filelist.sort()
    counter = 0
    dic = {}
    dic_for_sort_readen_order = {}

    for item in filelist:
        # item = item.split("/")[-1]
        counter += 1
        print(counter,item)
        content = read_from_localfile(item)
        books = single_page(content)
        for book in books:
            dic_for_sort_readen_order[book._name] = book.been_read_date
        start = item.index('#')
        item = item[:start]
        # 合并多页
        if item in dic:
            # print(item ,' already exist')
            dic[item] = dic[item] + books
        else:
            dic[item] = books
    # for i in books:
    #     i.displayDoubanBook()
    print('dic_for_sort_readen_order:len=',len(dic_for_sort_readen_order))
    circulate_readen_order(dic_for_sort_readen_order, dic)


    persistent_list_to_local(myconfig.filename02 + '.mypickle', dic, directory)
