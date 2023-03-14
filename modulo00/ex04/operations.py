# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarriga <abarriga@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 16:48:41 by abarriga          #+#    #+#              #
#    Updated: 2023/03/13 17:21:36 by abarriga         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 3:

	Sum = int(sys.argv[1]) + int(sys.argv[2])
	Difference = int(sys.argv[1]) - int(sys.argv[2])
	Product = int(sys.argv[1]) * int(sys.argv[2])
	Quotient = int(sys.argv[1]) / int(sys.argv[2])
	Remainder = int(sys.argv[1]) % int(sys.argv[2])

	print(f"Sum:        {Sum}")
	print(f"Difference: {Difference}")
	print(f"Product:    {Product}")
	if sys.argv[1] == 0 or sys.argv[2] == 0:
		print("Quotient: ERROR (division by zero)")
		print("Remainder: ERROR (modulo by zero)")
	else:
		print(f"Quotient:   {Quotient}")
		print(f"Remainder:  {Remainder}")
elif len(sys.argv) > 3:
	print("AssertionError: too many arguments")
else:
	print("AssertionError: only one argument")