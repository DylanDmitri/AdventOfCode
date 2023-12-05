import os
import sys
import time
import subprocess


def waitForChange():
    def checktime():
        return os.stat(FNAME).st_mtime

    current = checktime()
    while checktime() == current:
        time.sleep(0.016)


def create():
    print('make', FNAME)
    f = open(FNAME, 'w')
    f.close()
    os.chmod(FNAME, 0o777)


if __name__ == '__main__':
    FNAME = sys.argv[1]
    # if not os.path
    # if FNAME not in os.listdir():
    #     create()

    while True:
        subprocess.run(['python3', FNAME])
        print('\n', '='*20, '\n'*5)
        waitForChange()
