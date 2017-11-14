import os 
import time

#指定需要备份的文件
source = ['/mnt/hgfs/code/scheme']

#指定备份文件 的存储位置
target_dir = '/usr/swa/backup'

#备份文件压缩成zip
#压缩文件的名称由源文件和当前时间组成(os.sep为系统目录分隔符，提高了可移植性)
target = target_dir + os.sep + \
		 time.strftime('%Y%m%d%H%M%S') + '.zip'

#如果目标不存在就进行创建
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

#使用zip命令打包
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

#运行备份
print('Zip command is：')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
	print('Successful backup to',target)
else:
	print('Backup Failed')