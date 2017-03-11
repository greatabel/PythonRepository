from time import sleep
from common import persistent_list_to_local, read_persistentedlist_from_local, get_html,\
                   save_to_localfile_with_dir,read_from_localfile


def single_doulist_handle(name, url, directory, scrawler_pagelimit=3):
    print('in single_doulist_handle:',name, url)
    index = 0
    for i in range(0,scrawler_pagelimit):
        print(url + '/?start=' + str(index) + '&sort=time&sub_type=')
        # content = get_html(url + '/?start=' + str(index) + '&sort=time&sub_type=')
        content = b't'
        save_to_localfile_with_dir(directory, '@@@02' + name + '#page' + str(i), content)
        index += 25
        sleep(1)
