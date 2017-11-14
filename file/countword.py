def count_words(filename): # 计算一个文件有多上文字
	try:
		with open(filename) as file_obj:
			content = file_obj.read()
	except FileNotFoundError:
		msg = "sorry,the file "+filename+"not exits."
		print(msg) 
	else:
		words = content.split()
		numWords = len(words)
		print("The file "+filename+"has about "+str(numWords)+" words")

def count_word_times(filename,Sword): # 计算一个文件有多上文字
	global num
	try:
		with open(filename) as file_obj:
			content = file_obj.read()
	except FileNotFoundError:
		pass 
	else:
		words = content.split()
		numWords = len(words)
		num = words.count(Sword)
		print("The file "+filename+"has about "+str(numWords)+" words")
		print(str(num),str(num/numWords))




filenames =['txtfile\Alice in Wonderland.txt','txtfile\Gutenberg\'s The Yellow Wallpaper.txt','txtfile\liad of Homer.txt']
for filename in filenames:
	count_word_times(filename,'I')

