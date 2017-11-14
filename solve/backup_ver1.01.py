import os 
import time

#指定需要备份的文件
source = ['/mnt/hgfs/code/scheme']

#指定备份文件 的存储位置
target_dir = '/usr/swa/backup'

#如果目标不存在就进行创建
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

#备份文件压缩成zip
#将当前日期作为主备份目录下的子目录
today = target_dir + os.sep +time.strftime('%Y%m%d')
#将当前时间作为zip文件的文件名
now = time.strftime('%H%M%S')

#zip文件名称格式
target = today + os.sep + now + '.zip' 

#如果子目录不存在就进行创建
if not os.path.exists(today):
	os.mkdir(today)
	print('Successful created directory',today)

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