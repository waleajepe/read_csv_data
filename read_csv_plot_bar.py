"""
A module that reads a csv file and plots a pi chart using a csv, matplotlib and np module
"""
import matplotlib as plt
import numpy as np
import csv

file_name = 'bar_data.csv'
with open(file_name, "r") as file:
    reader = csv.reader(file)
    reading = list(reader)
country_dict = {list_values[0]: int(list_values[1]) for list_values in reading}
country = list(country_dict.keys())
values = list(country_dict.values())
fig = plt.figure(figsize=(10, 10))

plt.bar(country, values, color = 'blue', width=0.3)

plt.xlabel("Countries")
plt.ylabel("Values")
plt.show()
