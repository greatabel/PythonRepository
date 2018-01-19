import csv
import sql_generator_config


def read_file(filename):
    sns = []
    infile = open(filename, 'r')
    for line in infile:
        sns.append(line.rstrip())
    return sns

def generate_sql(sns):
    sql = ""
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
    sns = read_file('sn_demo.txt')
    sql = generate_sql(sns)
    print(sql)
    with open('insert_demo.sql', 'wt') as f:
        f.write(sql)


