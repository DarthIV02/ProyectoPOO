from restaurant import Restaurant

class IceCreamStand (Restaurant):
	def __init__ (self, restaurant_name, cuisine_type, *flavors): #Added flavors for the icecream
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors

	def show_flavors (self): #Prints all the flavors
		print("Our flavors are:")
		for flavor in self.flavors:
			print(f"\t-{flavor}")

ScoopsAhoy = IceCreamStand("Scoops Ahoy", "dessert", "vanilla", "strawberry", "chocolate")
ScoopsAhoy.show_flavors()
ScoopsAhoy.open_restaurant()
