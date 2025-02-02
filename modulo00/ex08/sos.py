# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarriga <abarriga@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 15:35:45 by abarriga          #+#    #+#              #
#    Updated: 2023/03/14 16:25:05 by abarriga         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

MORSE_CODE_DICT = {
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..',
    'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
    'M':'--', 'N':'-.', 'O':'---', 'P':'.--.',
    'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
    'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---',
    '3':'...--', '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.', '0':'-----', ' ':'/'
    }

if len(sys.argv) > 1:
	text = ""
	text_new = "" 
	text = " ".join(sys.argv[1:])
	for x in text.upper():
		if x in MORSE_CODE_DICT:
			text_new += MORSE_CODE_DICT[x] + " "
print(text)	
print(text_new)