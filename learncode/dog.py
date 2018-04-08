class Dog():
	"一次模拟小狗的简单尝试"
	def __init__(self,name,age):
		"初始化属性"
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.title()+"is now sitting.")
	def rool_over(self):
		print(self.name.title()+" rolled over!")


my_dog = Dog('willie',6)
your_dog = Dog('lucy',3)
print("My dog's name is "+your_dog.name.title()+".")
print("My dog's age is "+str(your_dog.age)+".")

my_dog.sit()
my_dog.rool_over()