# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 21:17:44 2024

@author: Dell
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

#It is used to read data from a CSV file
Df = pd.read_csv('22020085.csv')

#It shows the first five rows, allowing users to quickly inspect the structure and content of their data.
Df.head()  

# BAR GRAPH *******************************************************************************************************

# Create a group and Plotting Bar Graph
y = Df.groupby('Arrival station')['Average travel time (min)'].mean().sort_values().tail(10)
color = ['#74B72E', 'blue', '#74B72E', 'blue', '#74B72E', 'blue', '#74B72E', 'blue']

y.plot(kind = 'barh', color=color)

plt.xlabel('')
plt.ylabel('')
plt.title('Train Average Travel Time from Arrival Stations', fontdict={'fontsize': 14})

#LINE PLOT *******************************************************************************************************

# Create a group and calculate the mean for each group
Line_plot = Df.groupby('Month')[['Delay due to external causes', 
                        'Delay due to railway infrastructure',
                        'Delay due to traffic management',
                        'Delay due to station management and reuse of material',
                        'Delay due to travellers taken into account'
                        ]].mean().reset_index()

# Adding Figure
plt.figure()
plt.grid()
# Plotting a Line Plot
plt.plot(Line_plot, label='Line Plot', marker='.', linestyle='-')

# Adding labels and title
plt.xlabel('Months')
plt.ylabel('Number of Late Trains')
plt.title('No. of trains delayed over the months', fontdict={'fontsize': 12})

# Display a Output
plt.show()

# BAR GRAPH *******************************************************************************************************

# Create a Bar Graph
hbar_graph = Df.groupby('Year')['% trains late due to external causes (weather, obstacles, suspicious packages, malevolence, social movements, etc.)'
                       ].mean().sort_values().tail()
ax = hbar_graph.plot(kind='barh', figsize=(9,6), color=('red','slategrey'), zorder=4)

# Despine
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Switch off ticks
ax.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

# Draw vertical axis lines
vals = ax.get_xticks()
for tick in vals:
      ax.axvline(x=tick, linestyle='dashed', alpha=0.2, color='#eeeeee', zorder=1)

# Set x-axis label
ax.set_xlabel("", labelpad=20, weight='bold', size=12)

# Set y-axis label
ax.set_ylabel("", labelpad=20, weight='bold', size=12)

# Adding Title in Line Plot
plt.title('Percentage of Train Delays Due to External Causes', fontdict={'fontsize': 18})

# Donut Graph ******************************************************************************************************

# Set figure size
plt.figure(figsize=(10,15))

# explosion
explode = (0.05, 0.05, 0.05, 0.35, 0.05, 0.05, 0.04, 0.04, 0.04, 0.04)

# Create a pie chart
DDf = Df['Departure station']
DS = DDf.head(14)

DS.value_counts().plot(kind='pie', autopct='%1.1f%%', pctdistance=0.75, explode=explode, textprops={'weight': 'bold'})

font_prop = FontProperties(weight='bold')
plt.legend(prop=font_prop, bbox_to_anchor=(0,1))

# Draw circle
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig = plt.gcf()
 
# Adding Circle in Pie chart
fig.gca().add_artist(centre_circle)

plt.xlabel('2015', fontdict={'fontsize': 20})
# Adding Title in Pie chart
plt.title('Percentages (%) of Train Departure from Different Station in 2015', color='black', fontdict={'fontsize': 24})

plt.savefig('22020085.png', dpi=300)

#plt.show()