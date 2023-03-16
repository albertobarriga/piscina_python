from datetime import datetime
from recipe import Recipe

class Book:
	def __init__(self, name):
		self.name = name
		self.last_upd = datetime.now()
		self.crt_dt = datetime.now()
		self.rcp_lst = {"starter" : [], "lunch" : [], "dessert" : []}

	def get_recipe_by_name(self, name:str):
		"""Imprime la receta con el nombre \texttt{name} y devolver la instancia"""
		"""Busca las comidas que se encuentran dentro del diccionario y entonces las va
		ciclando hasta que encuentra la que sea igual que la busca y devuelve la receta"""
		if type(name) != str:
			return(print("error de tipo"))
		for meals in self.rcp_lst.values():
			for meal in meals:
				if (meal.name == name):
					print(str(meal))
					return (meal)
		return (None)

	def get_recipes_by_types(self, recipe_type:str) -> list:
		"""Devuelve todas las recetas dado un recipe_type """
		"""Verificamos si esta el tipo de comida en el diccionario y posteriormente hacemos
		una lista con las recetas que se encuentran dentro de un tpo de comida"""
		if recipe_type not in self.rcp_lst.keys():
			print("No esta la comida en el libro")
			return (None)
		meal_names = [meal.name for meal in self.rcp_lst[recipe_type]]
		return (meal_names)


	def add_recipe(self, recipe: Recipe) -> None:
		"""Añade una receta al libro y actualiza last_update"""
		"""Verificamos que la receta sea de la clase Recipe, buscas en el diccionario
		la key que cuadra con tu recipe_type y unes tu receta a esa key con append"""
		if not isinstance(recipe, Recipe):
			print("la receta no es el del tipo que debe de ser")
			return
		self.rcp_lst[recipe.rtype].append(recipe)
		self.last_upd = datetime.now()


