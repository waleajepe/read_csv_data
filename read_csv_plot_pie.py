"""
A module that reads a csv file and plots a pi chart using a csv, matplotlib and np module
"""
import matplotlib.pyplot as plt
import numpy as np
import csv

file_name = 'random_num.csv'
# Using the "with" keyword as it closes the file after reading through the data
with open(file_name, "r") as file:
    reader = csv.reader(file)
    reading = list(reader)
file_list = []
for list_value in reading[1:]:
    for value in list_value:
        file_list.append(value)

data = np.array(file_list)
fig = plt.figure(figsize=(10, 7))
plt.pie(x=data)
plt.show()
