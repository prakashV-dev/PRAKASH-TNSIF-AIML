import numpy as np

temperatures = np.array([28.5, 31.0, 29.5, 33.2, 30.1, 27.8, 32.4])
print("Daily Temperatures (°C):", temperatures)

avg_temp = np.mean(temperatures)
print("Average Temperature:", avg_temp)

highest_temp = np.max(temperatures)
lowest_temp = np.min(temperatures)
print("Highest Temperature:", highest_temp)
print("Lowest Temperature:", lowest_temp)

temps_above_30 = temperatures[temperatures > 30]
print("Temperatures above 30°C:", temps_above_30)

updated_temperatures = temperatures + 2
print("Updated Temperatures (+2°C):", updated_temperatures)
