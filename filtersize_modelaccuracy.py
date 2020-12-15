# Multiple line chart:
# https://python-graph-gallery.com/122-multiple-lines-chart/

import matplotlib.pyplot as plt
import os
import pandas as pd

fname = os.path.join("modelperf.csv")
the_df = pd.read_csv(fname)

# For both convolutional layers: 64 filters, 3 kernels, relu activation
percentages0 = the_df.loc[0][10:20].values
percentage_list0 = percentages0.tolist()

# For both convolutional layers: 32 filters, 3 kernels, relu activation
percentages1 = the_df.loc[1][10:20].values
percentage_list1 = percentages1.tolist()

# For both convolutional layers: 16 filters, 3 kernels, relu activation
percentages2 = the_df.loc[2][10:20].values
percentage_list2 = percentages2.tolist()

# For both convolutional layers: 8 filters, 3 kernels, relu activation
percentages3 = the_df.loc[3][10:20].values
percentage_list3 = percentages3.tolist()

# For both convolutional layers: 4 filters, 3 kernels, relu activation
percentages4 = the_df.loc[4][10:20].values
percentage_list4 = percentages4.tolist()

# For both convolutional layers: 2 filters, 3 kernels, relu activation
percentages5 = the_df.loc[5][10:20].values
percentage_list5 = percentages5.tolist()

epochs = [1,2,3,4,5,6,7,8,9,10]
plt.plot(epochs, percentage_list0, marker='o', markersize=4, color='red', linewidth=2, label='64')
plt.plot(epochs, percentage_list1, marker='o', markersize=4, color='green', linewidth=2, label='32')
plt.plot(epochs, percentage_list2, marker='o', markersize=4, color='blue', linewidth=2, label='16')
plt.plot(epochs, percentage_list3, marker='o', markersize=4, color='pink', linewidth=2, label='8')
plt.plot(epochs, percentage_list4, marker='o', markersize=4, color='black', linewidth=2, label='4')
plt.plot(epochs, percentage_list5, marker='o', markersize=4, color='turquoise', linewidth=2, label='2')
plt.suptitle('The Effect of Filter Size on Model Prediction Accuracy')
plt.legend()