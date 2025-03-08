import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# API configuration
# Replace with your own API key
API_KEY = 'c051f9e4877e393a4a3de7b7cd6c9b95'
CITY = 'Bhubaneswar'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

# Fetch weather data from the OpenWeatherMap API
response = requests.get(URL)
data = response.json()

# Process the API response
if response.status_code == 200:
    # Extract relevant weather information
    weather_data = {
        'City': data['name'],
        'Temperature (°C)': data['main']['temp'],
        'Humidity (%)': data['main']['humidity'],
        'Weather': data['weather'][0]['description']
    }
else:
    print("Error fetching data:", data.get("message", "Unknown error"))

# Convert the weather data to a pandas DataFrame for easy manipulation
df = pd.DataFrame([weather_data])
print(df)

# Set up the visual style for our charts
sns.set(style="whitegrid")

# Create a figure with two subplots side by side
plt.figure(figsize=(10, 5))

# Create a bar plot for temperature
plt.subplot(1, 2, 1)
sns.barplot(x='City', y='Temperature (°C)', data=df, palette='Blues')
plt.title('Temperature in °C')
plt.ylim(0, 40)  # Set y-axis limits for better visualization

# Create a bar plot for humidity
plt.subplot(1, 2, 2)
sns.barplot(x='City', y='Humidity (%)', data=df, palette='Greens')
plt.title('Humidity in %')
plt.ylim(0, 100)  # Set y-axis limits for percentage scale

# Adjust layout and display the plots
plt.tight_layout()
plt.show()