""" Patient's inflammation analysis for day 1 """

import numpy as np
import matplotlib.pyplot as ply

data = np.loadtxt(fname='data/inflammation1.csv', deliminter=',')

#Finding dimesions of data
print(data.shape)

print(data)

#Plotting data
image-1 = plt.plot(data)

plt.show(image-1)