import os
import os.path

def dfs_show(path,depth):
    if depth == 0:
        print(path)     #输出第一级目录

    pathlist = os.listdir(path)     #获取当前目录下的文件和目录

    for item in pathlist:
        if '.git' not in item:
            print("|  " * depth +"|___"+item)
            newitem = path+'\\'+item
            if os.path.isdir(newitem):      #判断是否为目录
                dfs_show(newitem,depth+1)   #递归深度优先遍历

if __name__ == '__main__':
    filepath = input("please enter path:")
    dfs_show(filepath,0)
