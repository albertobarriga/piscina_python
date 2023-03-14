# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarriga <abarriga@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 13:42:05 by abarriga          #+#    #+#              #
#    Updated: 2023/03/14 15:30:20 by abarriga         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string
	
if len(sys.argv) == 3:
	text = sys.argv[1]
	try:
		num = int(sys.argv[2])
	except:
		print("ERROR")
		exit()
	text_new = ""
	text_new = text.translate(str.maketrans("", "", string.punctuation))
	words = text_new.split(" ")
	words_ok = [word for word in words if len(word) > num]
	print(words_ok)
else:
	print("ERROR")

	