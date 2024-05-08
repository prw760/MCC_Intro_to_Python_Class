# Paul Wade
# PA 14

from matplotlib import pyplot as plt
import csv


# initialize empty sets
year_int = []
year_str = []
arizona = []
indiana = []
massachusetts = []
tennessee = []
washington = []

# open the data file, then read through it to fill the empty state data lists
with open('StatePopulation_19102020.csv', 'r') as population:

	reader = csv.reader(population)

	next(reader, None)              # Skip the header row

	for row in reader:
		year_int.append(int(row[0]))
		year_str.append(str(row[0]))
		arizona.append(int(row[1]))
		indiana.append(int(row[2]))
		massachusetts.append(int(row[3]))
		tennessee.append(int(row[4]))
		washington.append(int(row[5]))

# add the plot lines onto the chart
plt.plot(year_int, arizona, 'blue')
plt.plot(year_int, indiana, 'gold')
plt.plot(year_int, massachusetts, 'green')
plt.plot(year_int, tennessee, 'orange')
plt.plot(year_int, washington, 'purple')

# add the x-axis tick values / names
plt.xticks(year_int, year_str)

# add on title and axis lables
plt.title('Population from 1910 to 2020')
plt.xlabel('Year')
plt.ylabel('Population')

# include a legend mapping states to colors represented in the chart-plots
plt.legend(['Arizona', 'Indiana', 'Massachusetts', 'Tennessee', 'Washington'])

# render/show the chart
plt.show()
