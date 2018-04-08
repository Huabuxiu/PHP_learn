def total(a=5,*numbers,**pbook):
	print('a',a)
	for single_item in numbers:
		print('single_item',single_item)

	# print(pbook)

	for first_part,second_part in pbook.items():
		print(first_part,second_part)

print(total(10,1,2,3,jack=1123,john=2331,inge=1560))