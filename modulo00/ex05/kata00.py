# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarriga <abarriga@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 18:12:15 by abarriga          #+#    #+#              #
#    Updated: 2023/03/13 18:12:16 by abarriga         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata00.py file
kata = (19,42,21)
a = len(kata) - 1
if a > 0:
	print("The 3 numbers are: ", end='')
for x in kata:
	if a != 0:
		print(x, end=', ')
		a += -1
	else:
		print(x)