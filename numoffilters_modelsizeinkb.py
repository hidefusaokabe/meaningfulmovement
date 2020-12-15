import matplotlib.pyplot as plt
import pandas as pd
from pandas import read_csv
filename = 'filtersize_modelsize.csv'
data = read_csv(filename)

plt.suptitle('The Effect of Number of Filters on Model Size in Kilobytes')
plt.plot(data['filters'],data['kilobytes'])
plt.xlabel('Number of Filters')
plt.ylabel('Size of Model in Kilobytes')
plt.show()