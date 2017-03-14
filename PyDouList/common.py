import os
import pickle
import pprint
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import csv


def save_to_localfile(filename, content, directory='./'):
    # http://stackoverflow.com/questions/11700593/creating-files-and-directories-via-python
    with open(os.path.join(directory, filename), 'wb') as f:
        f.write(content)

def read_from_localfile(filename, directory='./'):
    with open(os.path.join(directory, filename), 'r') as myfile:
        content = myfile.read()
    return content

# def csv_printer_from_localfile_and_return_last_readen_order(filename, directory='./'):
#     with open(os.path.join(directory, filename), newline='') as csvfile:
#         reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#         lastrow = None
#         all_rows = []
#         for lastrow in reader:
#             # [0].split(',')
#             # print(lastrow[0].split(','))
#             if lastrow is not None: 
#                 all_rows.append(lastrow[0].split(','))
#         for row in all_rows:
#             print(row,row[0])
#         csv_writer_book_to_local(all_rows[1:], filename)
#         return lastrow

def csv_printer_from_localfile_and_return_last_row(filename, directory='./'):
    with open(os.path.join(directory, filename), newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        lastrow = None
        for lastrow in reader:
            # print(', '.join(lastrow)) 
            pass       
        return lastrow

def csv_writer_book_to_local(books, last_readen_order, filename):
    with open(filename, 'a') as csvfile:
        fieldnames = ['ReadenOrder', 'EntryDate','Category','BookName']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for book in books:
            writer.writerow({'ReadenOrder': last_readen_order + 1 + book.readen_order, 'EntryDate': book.been_read_date,
                             'Category':book.category, 'BookName':book.name})

# def csv_writer_book_to_local(rows, filename):
#     with open(filename, 'wt') as csvfile:
#         fieldnames = ['ReadenOrder', 'EntryDate','Category','BookName']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         from datetime import datetime
#         for row in rows:
#             date = datetime.strptime(row[1], "%Y/%m/%d") 
#             writer.writerow({'ReadenOrder': row[0], 'EntryDate': datetime.strftime(date, "%Y-%m-%d"),
#                              'Category':row[2], 'BookName':row[3]})

# def save_to_localfile(filename, content):
#     with open(filename, 'wt') as f:
#         f.write(content)


# def read_from_localfile(filename):
#     with open(filename, "r") as myfile:
#         content = myfile.read()
#     return content


def persistent_list_to_local(filename, dic, directory='./'):
    # http://www.cnblogs.com/pzxbc/archive/2012/03/18/2404715.html
    print('filename=',filename,'dic=',len(dic), 'directory=', directory)
    output = open(os.path.join(directory, filename), 'wb')
    pickle.dump(dic, output)
    output.close()


def read_persistentedlist_from_local(filename, directory='./'):
    pkl_file = open(os.path.join('./' + directory + '/', filename), 'rb')
    data = pickle.load(pkl_file)
    # pprint.pprint(data)
    return data

def get_html(url):
    try:
        request = Request(url, None, {"User-Agent": "Mozilla/5.0 AppleWebKit/537.36"})
        response = urlopen(request)
        data = response.read().decode('utf-8')
        print('len(data)=', len(data))
    except HTTPError as e:
        print('Error code: ', e.code)
    except URLError as e:
        print('Reason: ', e.reason)
    return data