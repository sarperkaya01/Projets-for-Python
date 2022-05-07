# -*- coding: utf-8 -*-

b=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]


def flat(b,f=[]):

    for i in b:
        if type(i) == list:
                
            flat(i)
                
        else:
            f.append(i)

    return f

print(flat(b))
