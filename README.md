# Heat map: how color may misinterpret the data
## The same temperature data visualized in 9 color palettes, paired by year for comparison.

A heat map is a graphical representation of data that uses a system of color-coding to represent different values. In this visualization, color is a core component, and the key point is choosing an appropriate color palette to match the data.
 
Let’s look at several heat maps of temperature in Sudbury, which were created from the same dataset. Nevertheless, because they are displayed in different color palettes, you will have various feelings and perhaps biases.
 
Here is how I feel the temperature in 9 maps (remember that in fact, all maps show the same temperature):
 
### 1st [coolwarm palette]: not hot summer and not cold winter, hot period is longer than cold period

![](Heat%20maps/1_coolwarm_cluster_heat_map.png)

### 2nd [rainbow palette]: hot summer and cold winter, hot period is shorter than cold period

![](Heat%20maps/2_rainbow_cluster_heat_map.png)

### 3rd [turbo palette]: very hot summer and a mix of cold and not cold winter, hot period is longer than cold period
 
![](Heat%20maps/3_turbo_cluster_heat_map.png)

### 4th [plasma palette]: very hot summer and not cold winter, hot period is longer than cold period

![](Heat%20maps/4_plasma_cluster_heat_map.png)

### 5th [magma palette]: not hot summer and very cold winter, hot period is longer than cold period

![](Heat%20maps/5_magma_cluster_heat_map.png)

### 6th [inferno palette]: very hot summer and very cold winter, hot period is longer than cold period
 
![](Heat%20maps/6_inferno_cluster_heat_map.png)

### 7th [summer palette]: hot summer and no winter, really?, hot period is longer than cold period

![](Heat%20maps/7_summer_cluster_heat_map.png)

### 8th [viridis palette]: not hot summer and a cold winter, hot period is shorter than cold period

![](Heat%20maps/8_viridis_cluster_heat_map.png)

### 9th [cividis palette]: hot summer and cold winter, hot period is longer than cold period
 
![](Heat%20maps/9_cividis_cluster_heat_map.png)

From my experience of living in Sudbury, I think no maps reflect the real temperature here. If I have to choose, the closest representation of Sudbury’s temperature is the second map (rainbow palette), although it should depict a much colder winter.
 
Note: 
- A large space between August and September 2020 is due to missing data from 8 am Aug 25 to 12 pm Sep 4.    
  Probably the weather station in Sudbury experienced some technical issues at that time.
- You may also notice that months are separated by spaces whose width varies by the number of days in the previous month. Thus, you will see:
  - The smallest gap after Jan, Mar, May, Jul, Aug, Oct (31 days)
  - A medium gap after Apr, Jun, Sep, Nov (30 days)
  - A big gap after Feb in a leap year (29 days)
  - And the biggest gap after Feb in a normal year (28 days).
- The heat maps were created with Matplotlib, a library for creating visualizations in Python.

---

**Data source:**
*Hourly Data Report – Environment and Climate Change Canada*

https://climate.weather.gc.ca/climate_data/hourly_data_e.html

The webpage shows data per day. However, you can download data per month by choosing a month, then click Go button, wait for data loading and when `month and year` in the line “Hourly Data (`month and year`)” displays your chosen month, it is ready to click Download Data button.
