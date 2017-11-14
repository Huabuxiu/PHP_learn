import os 
import time
import sys 
"""另一个可以增强的方向是在命令行中允许额外的文件与目录传递到脚本中。我们可以从
sys.argv 列表中获得这些名称，然后我们可以通过 list 类提供的 extend 方法把它们添加
到我们的 source 列表中"""
a = sys.argv[0]
print(a)
