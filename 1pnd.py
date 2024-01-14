import numpy as np
import pandas as pd

data = ["Pandas", "Matplotlib", "Numpy", 2, 5, 4.6, [1, 2, 3]]
s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(s)
# print(s[['b', 'c', 'f']])
print(s.index)
# print(s.__dict__)

# data1 = [[4, 7, 10], [5, 8, 8], [4, 33, 99]]
# df = pd.DataFrame(data1, index=['a', 'b', 'c'])


# print(df)


# from sys import argv

# script, a, b, c = argv

# print(script)
# print(a, b, c)
