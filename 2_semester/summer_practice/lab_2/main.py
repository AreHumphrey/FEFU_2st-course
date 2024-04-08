import numpy as np
import matplotlib.pyplot as plt

data_file = np.loadtxt('data.txt')

selected_values = data_file[5500:5600, 0:]

mean_values = np.mean(selected_values, axis=0)

normalized_values = selected_values / mean_values

normalized_values = np.nan_to_num(normalized_values)

plt.imshow(normalized_values, cmap='gist_stern', vmin=-4, vmax=4)
plt.show()
