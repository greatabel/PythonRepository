# coding=utf-8

def fib(max):
 a,b=1,1
 while a<max:
   yield a
   a,b=b,a+b

for n in fib(15):
  print n

print '*'*20,'another example'
import math
def is_prime(number):
 if number>1:
   if number==2:
    return True
   if number%2==0:
    return False
   for current in range(3,int(math.sqrt(number)+1),2):
    if number%current ==0:
     return False
   return True
 return False

def get_primes(input_list):
 result_list=list()
 for element in input_list:
   if is_prime(element):
    result_list.append(element)
 return result_list

def better_primes(input_list):
  return (element for element in input_list if is_prime(element))

def simple_generator_function():
 yield 1
 yield 3
 yield 5

for value in simple_generator_function() :
 print value
our_generator=simple_generator_function()
print next(our_generator),next(our_generator),'haha',next(our_generator)

print get_primes(range(1,10))
for i in better_primes(range(1,50)):
 print i

print '*'*20,'another example to do with infinite sequence'

def get_prime_with_yield(number):
 while True:
  if is_prime(number):
   yield number
  number+=1

def solve_number_10():
  total=2
  for next_prime in get_prime_with_yield(3):
   print next_prime,' ',
   if next_prime<100:
    total+=next_prime
   else:
    print 'total(prime)=',total
    return

solve_number_10()

print '*'*20,'PEP 342'


def get_primes1(number):
    while True:
        if is_prime(number):
            number = yield number
        number += 1


def print_successive_primes(iterations,base=10):
  prime_generator=get_primes1(base)
  prime_generator.send(None)
  for power in range(iterations):
   print prime_generator.send(base ** power)

print_successive_primes(5)


print '*'*20,"实际例子",'*'*20

import random
def get_data():
 """ 返回0~9之间的3个随机数"""
 return random.sample(range(10),random.randint(1,5))

def consume():
 """ 显示每次传入的整数的动态平均值"""
 running_sum = 0
 data_items_seen= 0
 while True:
  data = yield
  data_items_seen+= len(data)
  running_sum+=sum(data)
  print('The running average is {}'.format(running_sum/float(data_items_seen)))

def produce(consumer):
 """ 产生序列集合,传递给消费函数"""
 while True:
  data = get_data()
  print('Produced {}'.format(data))
  consumer.send(data)
  yield

if __name__ == '__main__':
   consumer = consume()
   consumer.send(None)
   producer = produce(consumer)
   for _ in range(10):
    print 'producting',next(producer)
