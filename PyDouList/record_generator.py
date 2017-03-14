from common import persistent_list_to_local, read_persistentedlist_from_local
import myconfig


def record_generator():
    print('----generate_record----')
    detailDic = read_persistentedlist_from_local(myconfig.filename02 + '.mypickle', myconfig.directory)
    books = []
    for key, single_doulist in detailDic.items():
        for idx, book in enumerate(single_doulist):
            # book.displayDoubanBook()
            books.append(book)
    # books.sort(key=lambda x: x.readen_order, reverse=True)
    books.sort(key=lambda x: x.readen_order)
    for book in books:
        book.displayDoubanBook()
    return ""