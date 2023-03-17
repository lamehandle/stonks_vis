import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as date
import numpy as np
import csv


# x = np.linspace(0, 2 * np.pi, 200)
# y = np.sin(x)
#
# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()


with open('C:\\Users\\james\\Downloads\\en_climate_daily_MB_5023227_2023_P1D.csv', 'r') as climate:
    csvreader = csv.DictReader(climate)

    dates = []
    temp = []
    for row in csvreader:
        dates.append(row["Date/Time"])
        temp.append(row["Max Temp"])

plt.plot(dates, temp)
plt.show()
