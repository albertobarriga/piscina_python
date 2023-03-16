import random

def generator(text, sep=" ", option=None):
	if (not text.isprintable() or not isinstance(text, str) or not isinstance(sep, str) or option not in [None, "shuffle", "unique", "ordered"]):
		return(print("Error"))
	text = text.split(sep)
	if option == "ordered":
		text = sorted(text)
		for word in text:
			yield(word)
	elif option == "shuffle":
		while len(text) > 0:
			i = random.randint(0, len(text) - 1)
			yield(text[i])
			text.remove(text[i])
	elif option == None:
		for word in text:
			yield(word)
	elif option == "unique":
		text = list(dict.fromkeys(text))
		for word in text:
			yield(word)

for word in generator("hola que tal que como te encuentras", " ", "shuffle"):
	print(word)
