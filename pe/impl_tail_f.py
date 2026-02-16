import os
import time

"""
Implement 'tail -f'
"""
with open("/tmp/01.txt", 'r') as f:
    f.seek(0, os.SEEK_END)


    while True:
        line = f.readline()
        if not line:
            time.sleep(1)
            continue

        print(line, end='')
