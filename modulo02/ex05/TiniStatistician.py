# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    TiniStatistician.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarriga <abarriga@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/27 17:13:12 by abarriga          #+#    #+#              #
#    Updated: 2023/03/27 20:53:08 by abarriga         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#CAlcula la media, mediana, quartiles, varianza y desviación estandar.

from math import sqrt

class TinyStatistician:
    def check_lst(func):
        def decorator(*args, **kwargs):
            lst = args[1]
            if not lst:
                return None
            return func(*args, **kwargs)
        return decorator
    
    @check_lst
    def mean (self, lst):
        sum = 0
        for i in lst:
            sum += i
        return (sum / len(lst))
    
    @check_lst
    def median(self, lst):
        lst = sorted(lst)
        n = len(lst)
        if n % 2 == 0:
            index1 = n // 2 - 1
            index2 = n // 2
            return float((lst[index1] + lst[index2]) // 2)
        else:
            index = n // 2
            return float(lst[index])
        
    @check_lst
    def quartile(self, lst):
        lst = sorted(lst)
        q1_index= int(len(lst) * 0.25)
        q3_index= int(len(lst) * 0.75)
        if len(lst) % 4 != 0:
            q1 = lst[q1_index]
            q3 = lst[q3_index]
        else:
            q1 = (lst[q1_index] + lst[q1_index + 1]) / 2
            q3 = (lst[q3_index] + lst[q3_index + 1]) / 2
        res = [float(q1), float(q3)]
        return res
    
    @check_lst
    def var(self, lst):
        lst = sorted(lst)
        med = self.mean(lst)
        sum = 0
        for i in lst:
            sum += (i - med)**2
        return sum/len(lst)
    
    @check_lst
    def std(self, lst):
        res = sqrt(self.var(lst))
        return res
        