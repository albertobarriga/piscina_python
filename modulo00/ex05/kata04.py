# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarriga <abarriga@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 18:47:35 by abarriga          #+#    #+#              #
#    Updated: 2023/03/13 19:02:28 by abarriga         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

print("module_%02d, ex_%02d, %.2f" % (kata[0], kata[1], kata[2]), end='')
s = "{:.2e}".format(kata[3])
print(", " + s, end='')
c = "{:.2e}".format(kata[4])
print(", " + c)