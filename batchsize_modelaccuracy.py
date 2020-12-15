import matplotlib.pyplot as plt
import os
import pandas as pd

fname = os.path.join("modelperf.csv")
the_df = pd.read_csv(fname)

# For both convolutional layers: 32 filters, 3 kernels, relu activation
percentages1 = the_df.loc[9][10:20].values
percentage_list1 = percentages1.tolist()

# For both convolutional layers: 16 filters, 3 kernels, relu activation
percentages2 = the_df.loc[10][10:20].values
percentage_list2 = percentages2.tolist()

# For both convolutional layers: 8 filters, 3 kernels, relu activation
percentages3 = the_df.loc[11][10:20].values
percentage_list3 = percentages3.tolist()

epochs = ['1','2','3','4','5','6','7','8','9','10']
plt.plot(epochs, percentage_list1, marker='o', markersize=4, color='red', linewidth=2, label='32')
plt.plot(epochs, percentage_list2, marker='o', markersize=4, color='green', linewidth=2, label='16')
plt.plot(epochs, percentage_list3, marker='o', markersize=4, color='blue', linewidth=2, label='8')
plt.suptitle('The Effect of Batch Size on Model Prediction Accuracy')
plt.legend()