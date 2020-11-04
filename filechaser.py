''' get the newest file from the folder'''

import os
import time
import shutil
import ntpath

def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

ntpath.basename("a/b/c")

def path_leaf(path):
    ''' to get the last name or the just file path'''
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def check_for_old_file(meta):
    """to check the exsistance of a file"""
    file_data = open("fileData.txt", "a+")
    file_data.seek(0)
    f = file_data.readlines()
    meta = meta+"\n"
    if meta in f:
        # file_data.seek(0)
        # print(file_data.readlines())
        file_data.close()
        return False
    else:
        file_data.write(meta + "\n")
        file_data.seek(0)
        return True
''' use SET data structure for unique file ????'''
def  pth():
    # while True
    ''' to get the filepath and file name'''
    filename = newest('ENTER PROJECT FOLDER PATH')
    meta = path_leaf(filename)
    old_check = check_for_old_file(meta)
    print('file_path: ', filename, ' ', 'meta_name: ', meta, ' ', 'checker:', old_check)
    return filename, meta, old_check

if __name__ == '__main__':
        pth()


