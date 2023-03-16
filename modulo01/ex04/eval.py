class Evaluator:
	
	@staticmethod
	def zip_evaluate(coefs, words):
		if not len(coefs) == len(words):
			return (-1)
		tu = []
		a = 0
		tu = list(zip(words, coefs))
		for i in tu:
			a += (len(tu[i][0]) * tu[i][1])
		print (a)
		

	# @staticmethod
	# def enumarate_value(coefs, words):
	# zip_evaluate([1,2], ["hola", "adios"])