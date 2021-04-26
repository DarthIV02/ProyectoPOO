from restaurant import Restaurant


class IceCreamStand (Restaurant):
	def __init__(self, restaurant_name, cuisine_type, toppings=None, *flavors):  # Added flavors for the ice cream
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors
		self.toppings = toppings

	def show_flavors(self):  # Prints all the flavors
		print("Our flavors are:")
		for flavor in self.flavors:
			print(f"\t-{flavor}")

	def show_toppings(self):
		if self.toppings is not None:
			print("Our toppings are:")
			for topping in self.toppings:
				print(f"\t-{topping}")


if __name__ == "__main__":
	ScoopsAhoy = IceCreamStand("Scoops Ahoy", "dessert", None, "vanilla", "strawberry", "chocolate")
	ScoopsAhoy.show_flavors()
	ScoopsAhoy.open_restaurant()

	print("\n")

	Thrifty = IceCreamStand("Thrifty", "dessert", ["Cherry", "crushed almonds"], "vanilla", "strawberry")
	Thrifty.show_toppings()
