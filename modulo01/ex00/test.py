from book import Book
from recipe import Recipe

a = Recipe("juan", 4, 2, ["awita"], "holaa", "lunch")
libro = Book("RECETARIO")
libro.add_recipe(a)
libro.get_recipe_by_name("juan")