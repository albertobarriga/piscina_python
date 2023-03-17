class Evaluator:
	
	@staticmethod
	def zip_evaluate(coefs, words):
		if not len(coefs) == len(words):
			return (-1)
		lst = []
		a = 0
		lst = list(zip(words, coefs))
		for i in lst:
			a += (len(i[0]) * i[1])
		return (a)

	@staticmethod
	def enumerate_evaluate(coefs, words):
		
		if not len(coefs) == len(words):
			return (-1)
		lst = []
		lst = list(enumerate(words))
		a = 0
		for i in lst:
			a += (len(i[1]) * coefs[i[0]])
		return(a)


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))
