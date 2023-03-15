from datetime import datetime

class Book:
	def __init__(self, name:str, last_upd:datetime, crt_dt:datetime, rcp_lst:dict):
		if len(name) == 0 or type(name) != str:
			return(print("Input error"))
		self.name = name
		if type(last_upd) != datetime:
			return(print("Input error"))
		self.last_upd = last_upd
		if type(crt_dt) != datetime:
			return(print("Input error"))
		self.crt_dt = crt_dt
		if type(rcp_lst) != dict:
			return(print("Input error"))
		if len(rcp_lst) != 3
		self.rcp_lst = rcp_lst

	def get_current_time
	def get_recipe_by_name(self, name:str):
		"""Imprime la receta con el nombre \texttt{name} y devolver la instancia"""
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
		if recipe_type not in self.rcp_lst.keys():
			print("No esta la receta en el libro")
			return (None)
		meal_names = [meal.name for meal in self.rcp_lst[recipe_type]]
		return (meal_names)


	def add_recipe(self, recipe: Recipe) -> None:
		"""Añade una receta al libro y actualiza last_update"""
		if not isinstance(recipe, Recipe):
			print("la receta no existe")
			return
		self.rcp_lst[recipe.recipe_type].append(recipe)
		self.last_upd = self.get_current_time()


