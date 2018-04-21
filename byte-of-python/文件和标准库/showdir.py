import os
import os.path

def dfs_show(path,depth):
    if depth == 0:
        print(path)

    pathlist = os.listdir(path)

    for item in pathlist:
        if '.git' not in item:
            print("|  " * depth +"|___"+item)
            newitem = path+'\\'+item
            if os.path.isdir(newitem):
                dfs_show(newitem,depth+1)

if __name__ == '__main__':
    filepath = input("please enter path:")
    dfs_show(filepath,0)
