import os
from pathlib import Path
from shutil import copyfile
from common import persistent_list_to_local, read_persistentedlist_from_local,\
                   csv_printer_from_localfile_and_return_last_row,\
                   csv_writer_book_to_local
import myconfig


def record_generator():
    print('----generate_record----')
    detailDic = read_persistentedlist_from_local(myconfig.filename02 + '.mypickle', myconfig.directory)

    books = []
    for key, single_doulist in detailDic.items():
        for idx, book in enumerate(single_doulist):
            # book.displayDoubanBook()
            books.append(book)
    books.sort(key=lambda x: x.readen_order)
    # books.sort(key=lambda x: x.readen_order, reverse=True)
    bookrecord_place = myconfig.file_wait_to_process_directory + '/' + myconfig.origin_bookrecords
    bookrecord_target = myconfig.file_outupt_directory + '/' + myconfig.origin_bookrecords
    
    print('bookrecord_place=',bookrecord_place)
    if Path(bookrecord_place).is_file():
        lastrow = csv_printer_from_localfile_and_return_last_row(bookrecord_place)
        last_readen_order = lastrow[0].split(',')[0]
        last_been_read_date = lastrow[0].split(',')[1]
        print(books[0].been_read_date ,'#'*5, last_been_read_date)
        if books[0].been_read_date >= last_been_read_date:
            csv_writer_book_to_local(books, int(last_readen_order), bookrecord_place)
            copyfile(bookrecord_place, bookrecord_target)
    # for book in books:
    #     book.displayDoubanBook()

    return ""