from exceptions import HourFormatException
from datetime import datetime


class Restaurant:
	"""A class for restaurants"""

	def __init__(self, restaurant_name, cuisine_type, opening_hours=None):  # All the attributes
		self.restaurant_name = restaurant_name.title()
		self.cuisine_type = cuisine_type
		self.number_served = 0
		self.opening_hours = opening_hours

	def describe_restaurant(self):
		"""Prints all of the atributes"""
		print(f"\nThe resaturant name is: {self.restaurant_name}")
		print(f"The cuisine type is: {self.cuisine_type}")

	def set_opening_hours(self, opening_hour: int, closing_hour: int):
		"""Manipulates the opening hours, the hour must be in 24 format"""
		try:
			if not 0 < opening_hour < 24 or not 0 < closing_hour < 24:
				raise HourFormatException
		except HourFormatException:
			print("The hour must be in 24 format")
		except TypeError:
			print("Value must be integer")
		else:
			self.opening_hours = [opening_hour, closing_hour]

	def check_if_restaurant_is_open(self):
		current_time = datetime.now()
		if self.opening_hours is not None:
			if self.opening_hours[0] <= int(current_time.hour) <= self.opening_hours[1]:
				print(f"The restaurant {self.restaurant_name} is currently open")
			else:
				print(f"The restaurant {self.restaurant_name} is currently closed")
		else:
			print(f"The opening hours of the restaurant {self.restaurant_name} are not defined")

	def open_restaurant(self):
		print(f"The restaurant {self.restaurant_name} is now open")

	def close_restaurant(self):
		print(f"The restaurant {self.restaurant_name} is now closed")

	def set_number_served(self, num):
		"""Changes the number of cutomers"""
		self.number_served = num

	def increment_number_served(self, num):
		"""Incrementes the number of cutomers"""
		self.number_served += num


if __name__ == "__main__":

	my_restaurant = Restaurant("yokomi sushi", "japanese")

	print(my_restaurant.restaurant_name)
	print(my_restaurant.cuisine_type)

	my_restaurant.set_opening_hours(16, 20)
	my_restaurant.check_if_restaurant_is_open()

	my_restaurant.describe_restaurant()
	my_restaurant.open_restaurant()

	your_restaurant = Restaurant("little cesar", "italian")
	your_restaurant.describe_restaurant()

	her_restaurant = Restaurant("la toscana", "mexican")
	her_restaurant.describe_restaurant()

	restaurant = Restaurant("Taikishi", "japanese")
	restaurant.describe_restaurant()
	print(restaurant.number_served)
	restaurant.number_served = 14
	print(restaurant.number_served)
	restaurant.set_number_served(25)
	print(restaurant.number_served)
	restaurant.increment_number_served(75)
	print(restaurant.number_served)
