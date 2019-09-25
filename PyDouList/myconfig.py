import datetime # NOQA

# 你的书籍存放目录，可以在该目录下文件和文件夹混放
file_wait_to_process_directory = '/Users/abel/Downloads/Study/alreadyReaden_Test'
# 你想要整理之后书籍文件夹和读书记录的目录
file_outupt_directory = '/Users/abel/Downloads/Study/alreadyReaden_Result'

# 原来的读书记录文件名字  文件放到书籍存放目录
origin_bookrecords = 'bookrecord.csv'

doulist_page = 'https://www.douban.com/people/greatabel/doulists/all'
doulist_prex = 'https://www.douban.com/doulist/'

scrawler_pagelimit = 1
scrawler_pagelimit_doulist = 2
last_async_time = '2019-08-27 12:15:14'
# I ignore @@@ started files in .gitignore
# filename01 = '@@@01my_all_doulist#'+datetime.datetime.today().strftime('%Y-%m-%d')

filename01 = '@@@01my_all_doulist#'
filename02 = '@@@02my_all_detail_doulist#'
blacklist = ['Fashion-Old', '我的收藏', 'magzine']
white_extension_name = ['.pdf', '.epub', '.mobi', '.txt']

directory = (datetime.datetime.today()).strftime('%Y-%m-%d')
# directory = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%Y-%m-%d')