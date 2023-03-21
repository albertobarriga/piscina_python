# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarriga <abarriga@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 11:03:31 by abarriga          #+#    #+#              #
#    Updated: 2023/03/21 12:44:30 by abarriga         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class CsvReader():
	def __init__(self, filename=None, sep=",", header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.file = None
		
	def __enter__(self):
		self.file = open(self.filename, "r")

	def __exit__(self, ):
		self.file.close()
		
	def getdata(self):
	""" Retrieves the data/records from skip_top to skip bottom.
	Return:
	nested list (list(list, list, ...)) representing the data.
	"""
	# ... Your code here ...
	
	def getheader(self):
	""" Retrieves the header from csv file.
	Returns:
	list: representing the data (when self.header is True).
	None: (when self.header is False).
	"""