# http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python

import glob
import os
filelist = glob.glob("*.png")
filelist.sort()
counter = 0
for item in filelist:
    # item = item.split("/")[-1]
    counter += 1
    print(counter,item)
    if counter >= 8 and counter <= 31:
        print('#',item ,"need change")
        new_name = str(int(item[:2])+51) + item[2:]
        os.rename(item, new_name)
    if counter > 31:
        new_name = str(int(item[:2])-24) + item[2:]
        print('new_name=',new_name)
        os.rename(item, new_name)
