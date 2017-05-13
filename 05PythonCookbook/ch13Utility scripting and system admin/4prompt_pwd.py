import getpass

def  svc_login(user, passwd):
    if user!="" and passwd!="":
        return True
    else:
        return False


def main():
    user = getpass.getuser()
    passwd = getpass.getpass()
    print('User:',user)
    print('Password:', passwd)
    
    if svc_login(user, passwd): 
        print('Yay!')
    else: 
        print('Boo!')

if __name__ == "__main__":
    main()