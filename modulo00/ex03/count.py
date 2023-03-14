# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarriga <abarriga@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 13:34:57 by abarriga          #+#    #+#              #
#    Updated: 2023/03/13 16:44:55 by abarriga         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def	text_analyzer(text = None):
	"""This function take only one argument and count the number of upper 
	characters, lower characters, punctuation and spaces in a given text."""
	if text == None:
		text = input("What is the text to analyze?")
	if type(text) != str:
		return print("AssertionError: argument is not a text")
	upper = 0
	lower = 0
	space = 0
	punct = 0
	for char in text:
		if char.isupper():
			upper += 1
		elif char.islower():
			lower += 1
		elif char == " ":
			space +=  1
		elif char == "." or char == "," or char == ":" or char == "!" or char == "¡":
			punct += 1
	print(f"The string contains {len(text)} character(s):")
	print(f"- {upper} upper letter(s)")
	print(f"- {lower} lower letter(s)")
	print(f"- {punct} punctuation mark(s)")
	print(f"- {space} spaces(s)")
	
if __name__ == '__main__':
	if len(sys.argv) > 2:
		print("AssertionError: argument is not a text")
	else:
		text_analyzer(sys.argv[1])
	
