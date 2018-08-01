import os
import scrapy
import csv
import json

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
                    if all(len(x) == len(sentences[0]) for x in sentences) and \
                    (len(sentences) == 4 or len(sentences) == 8) and \
                        row[0] != '' and row[0]!= 'article' and \
                        row[0] not in peoms:
                        print(row[0], '#'*10, sentences, len(sentences))
                        i += 1

                        peoms.append(row[0])
        print(i)
        # 根据诗句长度排序
        peoms.sort(key=len)
        print(peoms[0:20])
        peoms.sort(key=by_feeling_key,reverse=True)
        print(peoms[0:20])
        return peoms

# def csv_writer_book_to_local(peoms, filename):
#     with open(filename, 'a') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=['poem'])
#         writer.writeheader()
#         for poem in peoms:
#             writer.writerow({'poem': poem})

def write_to_json(poems, filename):
    with open(filename, 'a') as outfile:
        json.dump(poems, outfile, ensure_ascii=False)

def by_feeling_key(poem):
    sad = ['鸣', '薄命', '胸', '情人', '怜']
    happy = ['春', '美', '山', '田', '树', '鸟']
    count = 0
    for s in sad:
        if s in poem:
            count -= 4
    for h in happy:
        if h in poem:
            count += 1
    sentences = poem.replace('。', '，').split('，')
    if len(sentences) == 4:
        count += 2

    return count



poems = csv_printer_from_localfile('poems.csv', 'peom/')
# csv_writer_book_to_local(poems, 'processed.csv')
write_to_json(poems, 'poems.json')