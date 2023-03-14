# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarriga <abarriga@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 13:42:12 by abarriga          #+#    #+#              #
#    Updated: 2023/03/14 13:42:13 by abarriga         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

cookbook = {
	'bocadillo' : {"ingredients":["jamon", "pan", "queso", "tomate"], "meal": "almuerzo", "prep_time": "10"},
	'tarta' : {"ingredients":["harina", "azucar", "huevos"], "meal": "postre", "prep_time": "60"},
	'ensalada' : {"ingredients":["aguacate", "rucula", "tomates", "espinacas"], "meal": "almuerzo", "prep_time": "15"}
}
#print(cookbook["bocadillo"]["ingredients"])

def print_cookbook():
	for key in cookbook:
		print(key)

def print_recipe(key):
	if key in cookbook:
		print(f"Recipe for {key}")
		print("	Ingredients list:", cookbook[key]["ingredients"])
		print(f"	To be eaten for:", cookbook[key]["meal"])
		print(f"	Takes", cookbook[key]["prep_time"] ,"minutes of cooking.")

def eliminate_key(cookbook, key):
	if key in cookbook:
		del cookbook[key]

def add_key(cookbook):
	ingredients = []
	name = input("Enter a name:")
	ingredients = input("Enter ingredients:")
	meal = input("Enter a meal type:")
	try:
		time = int(input("Enter a preparation time:"))
	except:
		return(print("An exception occurred"))
	temp_dir = {
		name : {
			"ingredients": ingredients,
			"meal": meal,
			"prep_time": time
			}
	}
	cookbook.update(temp_dir)
	


print("Welcome to the Python Cookbook !")
print("List of available option:")
print("		1: Add a recipe")
print("		2: Delete a recipe")
print("		3: Print a recipe")
print("		4: Print the cookbook")
print("		5: Quit")
try:
	option = int(input("Please select an option:"))
except:
	print("Sorry, this option does not exist.")
	exit()
if option > 5 or option < 1:
	print("Sorry, this option does not exist.")
	exit()
if option == 1:
	add_key(cookbook)
elif option == 2:
	recipe = input("Please enter a recipe name to delete:")
	eliminate_key(cookbook, recipe)
elif option == 3:
	recipe = input("Please select an option:")
	print_recipe(recipe)
elif option == 4:
	print_cookbook()
elif option == 5:
	print("Cookbook closed. Goodbye !")


#print_cookbook()
#print_recipe("bocadillo")
#eliminate_key(cookbook, "bocadillo")
#print("ya he borrado")
#print_recipe("bocadillo")
#add_key(cookbook)
#print_cookbook()
#print_recipe("patata")