import matplotlib.pyplot as plt
import random

# Set the initial temperature
temperature = 50

# Set the maximum and minimum temperature limits
max_temp = 100
min_temp = 0

# Generate temperature data
num_data_points = 1000
days = range(num_data_points)
temperature_map = {}

for day in days:
    if temperature >= max_temp:
        temperature += random.uniform(-1.5, 1)
    elif temperature <= min_temp:
        temperature += random.uniform(-1.1, 1.5)
    else:
        temperature += random.uniform(-1, 1.1)
   
    temperature_map[day] = temperature

# Generate Fibonacci sequence
fibonacci = [1, 2]
while fibonacci[-1] <= num_data_points:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# Calculate the slopes using Fibonacci sequence
slopes = []

# Calculate the weights
fib_max = 34
max_weight = 0.15
num_remaining_levels = len(fibonacci) - fib_max
weight_increment = (1 - max_weight) / num_remaining_levels
weights = []

for level in range(len(fibonacci)):
    if level < fib_max:
        weight = max_weight * (level + 1) / fib_max
    else:
        weight = max_weight + (level - fib_max + 1) * weight_increment
    weights.append(weight)

# Calculate the slopes with weights
for level in range(len(fibonacci)):
    if fibonacci[level] > len(temperature_map) - 1:  # Check if Fibonacci level exceeds available data points
        break
   
    x1 = max(days) - fibonacci[level]
    y1 = temperature_map[x1]
   
    x2 = max(days)
    y2 = temperature_map[x2]
   
    slope = (y2 - y1) / (x2 - x1)
    weight = weights[level]  # Get the corresponding weight
   
    slopes.append(slope)
   
    print(f"Slope {level+1}: {slope} (Weight: {weight})  (x1={x1} - Fib Level: {fibonacci[level]}, y1={y1})  (x2={x2}, y2={y2})")

# Calculate the weighted average slope
weighted_average_slope = sum(weight * slope for weight, slope in zip(weights, slopes)) / sum(weights)

print(f"\nWeighted Average Slope: {weighted_average_slope}")

# Plot the temperature data
plt.plot(list(temperature_map.keys()), list(temperature_map.values()))
plt.xlabel('Days')
plt.ylabel('Temperature (°F)')
plt.title('Temperature Variation')
plt.grid(True)
plt.show()

# Print the temperature map
for day, temp in temperature_map.items():
    print(f"Day {day}: {temp}°F")
