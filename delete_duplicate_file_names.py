# Delete duplicate file names under given dir recursively

import os

print("Enter dir path : ", end="")
dir = input().strip()
d = {}

for root, dirs, files in os.walk(dir):
    flag = False

    for filename in files:
        if d.get(filename) == None:
            d[filename] = 1
        else:
            #Delete file
            path = os.path.join(root,filename)
            print('Deleting file path : ', path)
            os.remove(path)
            flag = True

    if flag and len(os.listdir(root)) == 0:
        print('No content in path : ',root)
        os.rmdir(root)



