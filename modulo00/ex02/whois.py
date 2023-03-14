# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarriga <abarriga@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 13:35:00 by abarriga          #+#    #+#              #
#    Updated: 2023/03/13 13:35:01 by abarriga         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 2 and sys.argv[1].isdigit():
	num = int(sys.argv[1])
	if num == 0:
		print("I'm Zero.")
	elif num % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")
else:
	print("AssertionError: argument is not an integer")
