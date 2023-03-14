# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarriga <abarriga@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 12:25:18 by abarriga          #+#    #+#              #
#    Updated: 2023/03/13 13:04:27 by abarriga         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

del sys.argv[0]
string = ""
for arg in sys.argv:
	string += " " + arg
rev_string = string[:0:-1]
rev_change_string = rev_string.swapcase()
print(rev_change_string)