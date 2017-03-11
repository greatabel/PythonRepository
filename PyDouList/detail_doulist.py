from time import sleep
import glob
import os
from common import persistent_list_to_local, read_persistentedlist_from_local, get_html,\
                   save_to_localfile_with_dir,read_from_localfile
from book import DoubanBook

def single_doulist_handle(name, url, directory, scrawler_pagelimit=3):
    print('in single_doulist_handle:',name, url)
    index = 0
    for i in range(0,scrawler_pagelimit):
        print(url + '/?start=' + str(index) + '&sort=time&sub_type=')
        content = get_html(url + '/?start=' + str(index) + '&sort=time&sub_type=')
        save_to_localfile_with_dir(directory, '@@@02' + name + '#page' + str(i), content)
        index += 25
        sleep(1)

def single_page(fileurl):
    book = DoubanBook('test', 'abel', '2017-03-03')
    book.displayDoubanBook()

def deal_with_folder_html(directory):
    print(directory)
    filelist = glob.glob( directory + "/*")
    filelist.sort()
    counter = 0
    for item in filelist:
        # item = item.split("/")[-1]
        counter += 1
        print(counter,item)
        single_page(item)

