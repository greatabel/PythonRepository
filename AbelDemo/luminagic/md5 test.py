import hashlib                    

sn_config = {
    'salt': 'luminagic',
    'sha_digits': 5,
    'source_digits': 24
}   

def sha(pw,salt):                     
    pw_bytes = pw.encode('utf-8')
    salt_bytes = salt.encode('utf-8')
    # print('len=', len(hashlib.sha256(pw_bytes + salt_bytes).hexdigest()))
    return hashlib.sha256(pw_bytes + salt_bytes).hexdigest() 

def generete_final_sn(source):
    fmd5 = sha(source, salt)
    final_sn = source + fmd5[:sn_config['sha_digits']]
    return final_sn

def check_sn_validation(sn):

    sn_should_be = generete_final_sn(sn[:sn_config['source_digits']], salt)
    return sn_should_be==sn
                                  
if __name__ == "__main__":

    final_sn = generete_final_sn('M0BGDB07004901A123456789')
    print(final_sn)
    print(check_sn_validation(final_sn))
    print(check_sn_validation('M0BGDB07004901A1234567899752d'))