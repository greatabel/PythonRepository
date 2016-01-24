import shutil

shutil.make_archive('myarchive_name', 'zip','myfold')

# 解压
shutil.unpack_archive('myarchive_name.zip')