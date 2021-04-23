class Restaurant:
	"""A class for restaurants"""

	def __init__(self, restaurant_name, cuisine_type):  #All the attributes
		self.restaurant_name = restaurant_name.title()
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Prints all of the atributes"""
		print(f"\nThe resaturant name is: {self.restaurant_name}")
		print(f"The cuisine type is: {self.cuisine_type}")

	def open_restaurant(self):
		print(f"The restaurant {self.restaurant_name} is now open")

	def set_number_served(self, num):
		"""Changes the number of cutomers"""
		self.number_served = num

	def increment_number_served(self, num):
		"""Incrementes the number of cutomers"""
		self.number_served += num

my_restaurant = Restaurant("yokomi sushi", "japanese")

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)


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