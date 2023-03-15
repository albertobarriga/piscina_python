class Recipe:
	def __init__(self, name, cl, ct, ing, desc, rtype):
		if len(name) == 0 or type(name) != str:
			return(print("Input error"))
		self.name = name
		if 1>cl>5 or type(cl) != int:
			return(print("Input error"))
		self.cl = cl
		if 0>cl or type(ct) != int:
			return(print("Input error"))
		self.ct = ct
		if type(ing) != list:
			return(print("Input error"))
		self.ing = ing
		if type(desc) != str:
			return(print("Input error"))
		if len(desc) == 0:
			self.desc = ""
		else:
			self.desc = desc
		if (rtype != "entrante" and rtype != "comida" and rtype != "postre") or len(rtype) == 0 or type(desc) != str:
			return(print("Input error del rtype"))
		self.rtype = rtype

	def __str__(self):
		"""Return the string to print with the recipe info""" 
		txt = f"Esta es la receta {self.name}"
		"""Your code here"""
		return txt
	

a = Recipe("juan", 4, 2, ["awita"], "holaa", "comida")
def print_information(a):
	print (a.name)
	print (a.ing)
	print (a.rtype)


print_information(a)
print(a)