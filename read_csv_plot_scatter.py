"""
A module that reads a csv file and plots a scatter chart using a csv, matplotlib and np module
"""
from matplotlib import pyplot as plt
import numpy as np
import csv

# Using the "with" keyword as it closes the file after reading through the data
with open("random_num.csv", "r") as file:
    reader = csv.reader(file)
    reading = list(reader)

x_axis = []
for list_value in reading[1:10]:
    for value in list_value:
        x_axis.append(int(value))

y_axis = []
for list_value in reading[10:19]:
    for value in list_value:
        y_axis.append(int(value))

plt.scatter(np.array(x_axis), np.array(y_axis), color="blue")
plt.show()