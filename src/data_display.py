import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
import lib.complex_plot as cp

data = loadmat('./src/data/in_out_SBRT2_direto.mat')

# print(data)

input_array = np.concatenate(np.array(data['in_extraction']))
output_array = np.concatenate(np.array(data['out_extraction']))

input_validation = np.concatenate(np.array(data['in_validation']))
output_validation = np.concatenate(np.array(data['out_validation']))

cp.complex_plane2(input_array[:20], 1, 'input.png')
cp.complex_plane2(output_array[:20], 1, 'output.png')
cp.complex_plane2(input_validation[:20], 1, 'input_validation.png')
cp.complex_plane2(output_validation[:20], 1, 'output_validation.png')
# # Ploting charts
# fig, ax = plt.subplots()

# plt.polar(input_array.real, input_array.imag, 'o',
#          label='Amplifier data', markersize=3)
# plt.polar(output_array.real, output_array.imag, 'o',
#          label='Amplifier data', markersize=3)
# plt.legend()
# ax.grid()
# ax.set(xlabel='input', ylabel='output', title='Amplifier data')
# fig.savefig("amplifier_data.png")
