class Car():
	"""docstring for car"""
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + self.model
		return long_name.title()
	
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + "miles on it.")

	def upate_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self,miles):
		self.odometer_reading += miles





		

"""the second Class"""
class ElectricCar(Car):
	def __init__(self,make,model,year):
		super(self,ElectricCar).__init__(make,model,year)
		self.battery = Battery()