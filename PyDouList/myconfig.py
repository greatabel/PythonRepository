import datetime # NOQA

file_wait_to_process_directory = '/Users/wanchang/Downloads/Study/alreadyReaden_Test'
file_outupt_directory = '/Users/wanchang/Downloads/Study/alreadyReaden_Result'

doulist_page = 'https://www.douban.com/people/greatabel/doulists/all'
doulist_prex = 'https://www.douban.com/doulist/'

# I ignore @@@ started files in .gitignore
# filename01 = '@@@01my_all_doulist#'+datetime.datetime.today().strftime('%Y-%m-%d')

filename01 = '@@@01my_all_doulist#'
filename02 = '@@@02my_all_detail_doulist#'
blacklist = ['Fashion-Old', 'abel的日记', 'magzine']
white_extension_name = ['.pdf', '.epub', '.mobi', '.txt']

directory = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')