import numpy as np

array = np.array([[['a','b','c'],['d','e','f'],['g','h','i']],
                 [['j','k','l'],['m','n','o'],['p','q','r']],
                 [['s','t','u'],['v','w','y'],['z','','']]
                 ])


word = array[1,2,0] + array[0,1,1] + array[0,1,0] + array[1,2,2] + array[1,1,2]


print(word)