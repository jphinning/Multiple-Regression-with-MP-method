import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

import lib.get_regression_matrix as rm
import lib.get_linear_combination as lc
import lib.plot_scattered_chart as ps

data = loadmat('./src/data/in_out_SBRT2_direto.mat')

input_array = np.concatenate(np.array(data['in_extraction']))
output_array = np.concatenate(np.array(data['out_extraction']))

input_validation = np.concatenate(np.array(data['in_validation']))
output_validation = np.concatenate(np.array(data['out_validation']))

# Parameters
p_range = int(input("Enter your value for p: ")) + 1
m_range = int(input("Enter your value for m: ")) + 1

# All lines combined
regression_matrix = rm.modify_input(p_range, m_range, input_array)

coeficient_array, residuals, rank, s = np.linalg.lstsq(
    regression_matrix, output_array, rcond=None)


validation_matrix = rm.modify_input(p_range, m_range, input_validation)

predicted_output = lc.multiply_matrix(validation_matrix, coeficient_array)

# Difference between output and input angles
angle_difference = np.angle(output_array, True) - np.angle(input_array, True)
print(angle_difference)

ps.get_scattered_chart(abs(input_array), angle_difference, 'AM-PM', 'AM-PM')
ps.get_scattered_chart(abs(input_array), abs(output_array), 'AM-AM', 'AM-AM')
