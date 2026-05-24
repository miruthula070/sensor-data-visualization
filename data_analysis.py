import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("clean_sensor_data.txt",header=None)
data.columns = ["Sensor_Value"]
print(data)
print(data.describe())

high_values = data[data["Sensor_Value"] > 50]
print(high_values)
high_values.to_csv("high_sensor_values.csv", index = False)
plt.plot(data["Sensor_Value"])
plt.title("Sensor Dataset")
plt.ylabel("Data")
plt.xlabel("Index")
plt.grid(True)
plt.plot(data["Sensor_Value"], color="blue", label="Sensor Trend")
plt.scatter(high_values.index, high_values["Sensor_Value"], color="red", label="Anomaly (>50)")
plt.legend()
plt.show()