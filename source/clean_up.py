import os, shutil

path = 'raw_data/'

listdirs = os.listdir(path)
number_dirs = len(listdirs)

def cleaner():
    for i in range(1,number_dirs):
        path_dirs = path + "board_" + str(i) + "/result"
        if os.path.isdir(path_dirs):
            shutil.rmtree(path_dirs)
        path_score = path + 'board_' + str(i) + '/score.txt'
        try:
            os.unlink(path_score)
        except:
            pass

if __name__ == '__main__':
    cleaner()
    print("Finished cleaning up")