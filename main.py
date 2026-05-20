import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import calendar

# for the legend
import matplotlib.colors as mc
from matplotlib.cm import ScalarMappable

cmap = "cividis"

data = pd.read_csv('Sudbury temperature 2020-2021.csv', sep=',', on_bad_lines='skip')

# make sure data["date"] is of a datetime type.
data["date"] = pd.to_datetime(data["date"])

'''
It is very important to use the minimum and maximum temperature for all the heatmaps so the same colormap is applied to all the panels and they can be compared. Otherwise, Matplotlib creates a different colormap for each panel and the result would be misleading.
'''

MIN_TEMP = data["temp"].min()
MAX_TEMP = data["temp"].max()

def single_plot(data, month, year, ax):
    data = data[(data["date"].dt.year == year) & (data["date"].dt.month == month)]

    # Extract hour, day, and temperature
    hour = data["hour"]
    day = data["date"].dt.day
    temp = data["temp"]

    # Re-arrange temperature values
    temp = temp.values.reshape(24, len(day.unique()), order="F")

    # Compute x and y grids, which are passed to ax.pcolormesh().

    # The inner + 1 increases the length
    # The outer + 1 ensures days start at 1, and not at 0.
    xgrid = np.arange(day.max() + 1) + 1
    # Hours start at 0, end at 24
    ygrid = np.arange(25)
    
    ax.pcolormesh(xgrid, ygrid, temp, cmap=cmap, vmin=MIN_TEMP, vmax=MAX_TEMP)
  
    # Invert the vertical axis
    ax.set_ylim(24, 0)
  
    # Set tick positions for both axes
    ax.yaxis.set_ticks([i for i in range(24)]) # 0 to 23
    ax.xaxis.set_ticks([10, 20, 30])
  
    # Remove ticks by setting their length to 0
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)

    # Set labels of month
    if year == 2020:        
        month_name = calendar.month_abbr[month]
        ax.set_title(month_name, fontsize=14)

    # Set labels of year
    ax.yaxis.set_label_position("right")
    if month == 12:
        ax.set_ylabel(year, fontsize=14)
      
    # Remove all spines
    ax.set_frame_on(False)

# create a figure with 2 rows and 12 columns and loop through each month
# constrained_layout=True to prevent labels of different axes from overlapping each other
fig, axes = plt.subplots(2, 12, figsize=(14, 10), sharex=True, sharey=True, constrained_layout=True)

for y, year in enumerate([2020, 2021]):
    for m, month in enumerate(range(1, 13)): # 1 to 12
        single_plot(data, month, year, axes[y, m])

# Adjust margin and space between subplots
# Extra space is on the left to add a label
# Notice: subplots_adjust will disable constrained_layout
fig.subplots_adjust(left=0.05, right=0.97, top=0.89, hspace=0.08, wspace=0.04)

'''
Creating a color bar legend
'''
# Make room for the legend at the bottom.
fig.subplots_adjust(bottom=0.15)

# Create a new axis to contain the color bar
# Values are:
# (x coordinate of left border, 
#  y coordinate for bottom border,
#  width,
#  height)
cbar_ax = fig.add_axes([0.3, 0.05, 0.4, 0.02])

# Create a normalizer that goes from minimum to maximum temperature
norm = mc.Normalize(MIN_TEMP, MAX_TEMP)

# Create the colorbar and set it to horizontal
cb = fig.colorbar(
    ScalarMappable(norm=norm, cmap=cmap), 
    cax=cbar_ax, # Pass the new axis
    orientation = "horizontal"
)

# Remove tick marks
cb.ax.xaxis.set_tick_params(size=0)

# Set legend label
cb.set_label("Temperature (°C)", size=12)
'''
End of creating a color bar legend
'''

# Set common labels for x and y axes
fig.text(0.5, 0.1, "Day in month", ha="center", va="center", fontsize=14)
fig.text(0.02, 0.5, 'Hour (UTC−05:00)', ha="center", va="center", rotation="vertical", fontsize=14)

# Set the title
fig.suptitle(f"Heat map #9 [{cmap}] Temperature (°C) in Sudbury, Ontario, 2020-2021 (Thuc Dao)", fontsize=20, y=0.97)

# Save the plot as an image
fig.set_facecolor("white")
fig.savefig("Temperature in Sudbury, 2020-2021, made by Thuc Dao.png", dpi=300)