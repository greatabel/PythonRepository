record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email , *phone_numbers = record
print(phone_numbers)

*trailing, current = [10,1,2,3,4]
print(trailing,"|",current)

#-----------2-------
records = [
         ('foo', 1, 2),
         ('bar', 'hello world!'),
         ('foo', 3, 4),
    ]
def do_foo(x, y): print('foo$', x, y)
def do_bar(s): 
    print('bar#', s)

for tag, *args in records: 
    if tag == 'foo':
        do_foo(*args) 
    elif tag == 'bar':
        do_bar(*args)

#------3-----------
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homdir, sh = line.split(':')
print(uname,"|", fields , "|", homdir, "|",sh)

#-----4---------
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum([1,2,3,4]))