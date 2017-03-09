import datetime
import argparse
import hashlib    
import random
from string import ascii_uppercase, ascii_lowercase, digits
import subprocess

color_dic = {
    # we may add in future
    'Purple': 'P',
    'Green': 'G',
    'Pink': 'F',
    'Flamingo': 'F',
    'Blue': 'B',
    'Yellow': 'Y'
}

vendor_dic = {
    'Meomo': '01',
    'Putao': '02',
    'Guangzhou-kaixuan': '03'
}

sn_config = {
    'salt': 'luminagic',
    'sha_digits': 5,
    'source_digits': 24
}   
sn_prefix_url = 'https://app-exp.meomo.cn/#!/register/' 

def sha(pw,salt):                     
    pw_bytes = pw.encode('utf-8')
    salt_bytes = salt.encode('utf-8')
    # print('len=', len(hashlib.sha256(pw_bytes + salt_bytes).hexdigest()))
    return hashlib.sha256(pw_bytes + salt_bytes).hexdigest() 

def add_validation_to_sn(source, salt):
    sha_str = sha(source, salt)
    final_sn = source + sha_str[:sn_config['sha_digits']]
    return final_sn

def check_sn_validation(sn, salt):

    sn_should_be = generete_final_sn(sn[:sn_config['source_digits']], salt)
    return sn_should_be==sn


def revert_to_date_from_sn(sn):
    year = ord(sn[4]) - ord('A') + 2014
    month = ord(sn[5]) - ord('A') + 1
    day = int(sn[6:8])
    datetime_object = datetime.datetime.strptime('{}-{}-{}'.format(year, month, day), '%Y-%m-%d')
    return datetime_object

def random_string(digit_len):
    s = ascii_uppercase + digits + ascii_uppercase
    return ''.join(random.sample(s,digit_len))

def genereate_devicetoken(args, last_serial_number=0):
    # 12 character, this first 2 is M0 is fixed.
    # 3rd is SKU, current version is A, follow-up version is B, professional version is C ,etc.
    # 4th is color, P=Purple, G=Green F=Flamingo(Pink) B=Blue
    # 5th is produce year, 2014 is A, 2015 is B ,etc
    # 6th is produce month, ABCDEFGHIJKL presents 12 months
    # 7th and 8th are produce day, 01~31
    # 9th ~ 12th are produce day's serial number, 0001~9999
    fixed_sn = 'M0'
    year = chr(ord('A') + args.pdate.year - 2014)
    month = chr(ord('A') + args.pdate.month - 1)
    day = '{0:02}'.format(args.pdate.day)
    sn_list = []
    for i in range(int(args.num)):
        sn = fixed_sn + args.sku.upper() + color_dic[args.color] \
            + year + month + day + '{0:04}'.format(i+1+last_serial_number)
        sn = sn + vendor_dic[args.vendor] + random_string(10)
        final_sn =  add_validation_to_sn(sn, sn_config['salt'])
        # print('final=',final_sn)
        sn_list.append(final_sn)
    return sn_list


def valid_date(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

def sn_generator():
    parser = argparse.ArgumentParser(description='sku(type)  color pdate(produce date)')
    parser.add_argument('-sku', dest='sku', default="A", required=True, type=str)
    parser.add_argument('-color', dest='color', default="P",required=True, type=str)
    parser.add_argument('-vendor', dest='vendor', default="Putao",required=True, type=str)
    parser.add_argument('-pdate', dest='pdate', default="2017-01-10",
                        help="The Start Date - format YYYY-MM-DD ", 
                        required=True, type=valid_date)
    parser.add_argument('-num', dest='num', default="A", required=True, type=int)
    parser_result = parser.parse_args()
    print(parser_result.sku, parser_result.color, parser_result.pdate)
    sn_list = genereate_devicetoken(parser_result)
    # print(sn_list)
    for sn in sn_list:
        print_sn = sn_prefix_url + sn
        print(print_sn)
        bashCommand = "myqr "+ print_sn + " -n "+ sn + ".jpg  -d ./sns"
        output = subprocess.check_output(['bash','-c', bashCommand])



if __name__ == '__main__':
    # python3 sn_generator0.0.1.py -color="Green" -pdate='2017-02-15' -sku='B' -num=50 -vendor='Meomo'
    sn_generator()
