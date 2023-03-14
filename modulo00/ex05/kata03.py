# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata03.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarriga <abarriga@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 18:40:43 by abarriga          #+#    #+#              #
#    Updated: 2023/03/13 18:46:36 by abarriga         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata03.py file
kata = "The right format"

a = 41 - len(kata)
for x in range(0,a):
	print("-", end="")
print(kata)