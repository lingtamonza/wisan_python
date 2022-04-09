#บทเรียนการสร้างคลาส,เมธอด.แอททริบิวต์ โดยวิสาน กาฬพันธ์ ครูโรงเรียนค่ายประจักษ์ศิลปาคม
class Car():
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year

		self.fuel_capacity = 15
		self.fuel_level = 0

	def fill_tank(self):
		self.fuel_level=self.fuel_capacity
		print('Fule tank is full.')

	def drive(self):
		print('The car is moving.')

my_new_car = Car('audi','a4',2016)
my_new_car.fuel_level=10
print(f'Your car brand : {my_new_car.make}')
print(f'Your car model : {my_new_car.model}')
print(f'Your car year : {my_new_car.year}')

#การเรียกใช้เมธอด
my_new_car.fill_tank()
print(f'Your fuel level {my_new_car.fuel_level}')
my_new_car.drive()