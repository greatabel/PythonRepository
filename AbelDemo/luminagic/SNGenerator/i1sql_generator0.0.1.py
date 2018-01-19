import csv
import sql_generator_config
import os

def read_file(filename):
    sns = []
    infile = open(filename, 'r')
    for line in infile:
        sns.append(line.rstrip())
    return sns

def generate_sql(sns):
    sql = "use sharingan;\n"
    for sn in sns:
        source = 'Meomo'
        if len(sn) == 12:
            source = 'Putao'
        istr = "insert into devices(`sn`,`source`,`created_date`) \
select * from ( select '"+ sn + "','"+ source + "',now() ) as tmp \
WHERE NOT EXISTS (\
    SELECT `sn` FROM devices WHERE `sn` = '"+ sn +"' \
) LIMIT 1;\n"
        sql += istr
    return sql

if __name__ == '__main__':
    sns = read_file('SNS/sn.txt')
    sql = generate_sql(sns)
    print(sql)
    sql_file = 'SNS/insert.sql'
    if os.path.isfile(sql_file):
        os.remove(sql_file)
    mode = 'a' if os.path.exists(sql_file) else 'w'
    with open(sql_file, mode) as f:
        f.write(sql)


