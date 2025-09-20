# Create a tuple for weather data
weather = (1, 0, 0, 0, 1, 1, 0)

# Initalize counters
rainy = 0
sunny = 0

# Count rainy (1) and sunny (0) days
for day in weather:
    if day == 1:
        rainy += 1
    else:
        sunny += 1

print("Rainy days:", rainy)
print("Sunny days:", sunny)

# Predict the weather
if rainy > sunny:
    print("Prediction: Mostly Rainy🌧️")
elif sunny > rainy:
    print("Prediction: Mostly Sunny☀️")
else:
    print("Prediction: Equal chances of Rainy and Sunny⛅")

