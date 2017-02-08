import hashlib                    
                                  
def md5sum(pw,salt):                     
    pw_bytes = pw.encode('utf-8')
    salt_bytes = salt.encode('utf-8')
    return hashlib.sha256(pw_bytes + salt_bytes).hexdigest() 

                                  
if __name__ == "__main__":        
    fmd5 = md5sum('M0BGDB070049A12345678','luminagic')  
    print(fmd5, 'M0BGDB0700491234567890'+'#1'+fmd5[:5])