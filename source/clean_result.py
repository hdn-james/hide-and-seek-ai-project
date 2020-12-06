import os, shutil

path = 'raw_data/'

listdirs = os.listdir(path)
number_dirs = len(listdirs)

def cleaner():
    for i in range(number_dirs):
        path_dirs = path + "board_" + str(i) + "/result"
        if os.path.isdir(path_dirs):
            shutil.rmtree(path_dirs)

if __name__ == '__main__':
    cleaner()