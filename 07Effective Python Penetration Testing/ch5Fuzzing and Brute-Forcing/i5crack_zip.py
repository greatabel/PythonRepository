# osx 下带密码加密zip
# zip -e test.zip test.txt

import zipfile
filename = 'test.zip'
dictionary = 'passwordlist.txt'
password = None
file_to_open = zipfile.ZipFile(filename)
with open(dictionary, 'r') as f:
  for line in f.readlines():
        password = line.strip('\n')
        print('pass->', password)
        try:
              file_to_open.extractall(pwd=password.encode( ))
              password = 'Password found: %s' % password
              print(password)
        except Exception as ex:
            print(ex)
            pass
