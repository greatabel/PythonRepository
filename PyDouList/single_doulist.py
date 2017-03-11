from time import sleep
from common import persistent_list_to_local, read_persistentedlist_from_local, get_html,\
                   save_to_localfile,read_from_localfile


def single_doulist_handle(name, url, scrawler_pagelimit=3):
    print('in single_doulist_handle:',name, url)
    index = 0
    for i in range(0,3):
        print(url + '/?start=' + str(index) + '&sort=time&sub_type=')
        content = get_html(url + '/?start=' + str(index) + '&sort=time&sub_type=')
        save_to_localfile('@@@02' + name + '#page' + str(i), content)
        index += 25
        sleep(2)
