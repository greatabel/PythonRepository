import os
import scrapy
import csv

print(scrapy.version_info)

def csv_printer_from_localfile(filename, directory='./'):
    with open(os.path.join(directory, filename), newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        for row in reader:
            if row:
                if row[0] is not None and row[0] != "\"":
                    sentences = row[0].replace('。', '，').split('，')
                    print(row[0], '#'*10, sentences)
                    i += 1
        print(i)

def csv_writer_book_to_local(books, last_readen_order, filename):
    with open(filename, 'a') as csvfile:
        fieldnames = ['ReadenOrder', 'EntryDate','Category','BookName']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for book in books:
            writer.writerow({'ReadenOrder': last_readen_order + 1 + book.readen_order, 'EntryDate': book.been_read_date,
                             'Category':book.category, 'BookName':book.name})

csv_printer_from_localfile('poems.csv', 'peom/')