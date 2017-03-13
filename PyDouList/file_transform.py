import os

def file_transform(filepath, from_directory, to_directory, doulist_category):
    from_file = filepath
    print('doulist_category', doulist_category)
    to_file = to_directory + '/' + doulist_category +\
             '/' + filepath.rsplit('/', 1)[1]

    # print(from_file,' --> ',to_file)
    # to move only files, not folders
    if os.path.isfile(from_file):
        if not os.path.exists(to_directory):
            os.makedirs(to_directory)
        if not os.path.exists(to_directory +'/' + doulist_category):
            os.makedirs(to_directory +'/' + doulist_category)
        os.rename(from_file, to_file)
