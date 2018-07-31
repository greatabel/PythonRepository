import os
import scrapy
import csv

print(scrapy.version_info)

def csv_printer_from_localfile(filename, directory='./'):
    with open(os.path.join(directory, filename), newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        peoms = []
        for row in reader:
            if row:
                if row[0] is not None and row[0] != "\"":
                    # 去掉（ 和 之后的脏字符串
                    row[0] = row[0].split('(', 1)[0]
                    # 去掉。造成的错误断句
                    sentences = row[0].replace('。', '，').split('，')
                    # 去掉。造成的最后一个空句
                    if '' in sentences:
                        sentences.remove('')
                    # 去掉不是每句长度一致的词
                    if all(len(x) == len(sentences[0]) for x in sentences):
                        print(row[0], '#'*10, sentences, len(sentences))
                        i += 1
        print(i)

def csv_writer_book_to_local(books, last_readen_order, filename):
    with open(filename, 'a') as csvfile:

        writer = csv.DictWriter(csvfile)
        for book in books:
            writer.writerow({'ReadenOrder': last_readen_order + 1 + book.readen_order, 'EntryDate': book.been_read_date,
                             'Category':book.category, 'BookName':book.name})

csv_printer_from_localfile('poems.csv', 'peom/')