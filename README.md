# Hawaii Climate Analysis

## Table of Contents
- [Exploratory Precipitation Analysis](#exploratory-precipitation-analysis)
- [Exploratory Station Analysis](#exploratory-station-analysis)
- [Climate App](#climate-app)
- [Conclusions](#conclusions)

### Overview

This project analyzes climate data from August 2016 to August 2017 using a local database. It provides statistical insights and visualizations of precipitation and temperature patterns. Additionally, a climate app is developed to explore weather data, including recent precipitation, station information, and temperature records, with options to query specific date ranges.

### Exploratory Precipitation Analysis

#### Precipitation Bar Chart
![Precipitation Bar Chart](https://github.com/pixare7/sqlalchemy-project/blob/main/images/fig1.png)

**Figure 1:**  
This bar chart displays the precipitation (in inches) from August 23, 2016, to August 23, 2017.

#### Summary Statistics Table
![Summary Statistics Table](https://github.com/pixare7/sqlalchemy-project/blob/main/images/fig2.png)

**Figure 2:**  
The data for the same time period shows a mean precipitation of 0.177 inches and a standard deviation of 0.461 inches, indicating a wide spread in the precipitation values.

### Exploratory Station Analysis

#### Temperature vs. Frequency Bar Chart
![Temperature vs. Frequency Bar Chart](https://github.com/pixare7/sqlalchemy-project/blob/main/images/fig3.png)

**Figure 3:**  
This bar chart represents the frequency of temperatures recorded at the most active station, USC00519281, over the year. The temperature around 75°F was observed most frequently.

### Climate App

#### Overview

The climate app provides routes to explore weather data, including precipitation, stations, and temperature observations. Users can also retrieve the minimum, maximum, and average temperatures for a specific date range.

#### Available Routes

![Available Routes](https://github.com/pixare7/sqlalchemy-project/blob/main/images/fig4.png)

The climate app provides several routes to explore the weather data:

![Precipitation](https://github.com/pixare7/sqlalchemy-project/blob/main/images/fig5.png)

- **Precipitation:**  
  Access the last 12 months of precipitation data as a dictionary, where dates are keys and precipitation (in inches) are values.

![Stations](https://github.com/pixare7/sqlalchemy-project/blob/main/images/fig6.png)

- **Stations:**  
  Retrieve a list of all local weather stations.

![Temperature](https://github.com/pixare7/sqlalchemy-project/blob/main/images/fig7.png)

- **Temperature (TOBS):**  
  View the recorded temperatures for the most active station, USC00519281, including dates and temperatures observed.

![Minimum, Maximum, and Average Temperature (Start Date)](https://github.com/pixare7/sqlalchemy-project/blob/main/images/fig8.png)

- **Minimum, Maximum, and Average Temperature (Start Date):**  
  Input a start date to receive the minimum, maximum, and average temperatures from that date until the last date in the dataset.

![Minimum, Maximum, and Average Temperature (Start and End Date)](https://github.com/pixare7/sqlalchemy-project/blob/main/images/fig9.png)

- **Minimum, Maximum, and Average Temperature (Start and End Date):**  
  Input both start and end dates to get the minimum, maximum, and average temperatures for the specified date range.

## Conclusions

- **Precipitation Analysis:** The precipitation data from August 2016 to August 2017 shows significant variability, with a mean of 0.177 inches and a wide spread, indicating irregular rainfall patterns throughout the year.

- **Temperature Analysis:** The most active station, USC00519281, recorded temperatures most frequently around 75°F, suggesting a moderate climate in the area during the study period.

- **Climate App Utility:** The climate app effectively allows users to explore key weather data, making it easier to access historical precipitation and temperature records, as well as perform specific queries on temperature trends over time.
