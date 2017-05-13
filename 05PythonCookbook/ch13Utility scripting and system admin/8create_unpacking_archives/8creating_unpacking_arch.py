import shutil

print(shutil.get_archive_formats())
shutil.make_archive('myarchive_name', 'zip','myfold')

# unpack
shutil.unpack_archive('myarchive_name.zip')