import requests, json, os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

today = datetime.today()
week_ago = datetime.today() - timedelta(days=7)

today = today.date().isoformat()
week_ago = week_ago.date().isoformat()

def get_weather(latitude, longitude, start, end):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&start_date={start}&end_date={end}&daily=temperature_2m_max,temperature_2m_min"
    response = requests.get(url)
    data = response.json()
    return data

data = get_weather(32.249403, 35.258808, week_ago, today)


days = data['daily']['time']

min_temp = data['daily']['temperature_2m_min']
max_temp = data['daily']['temperature_2m_max']

df = pd.DataFrame({
    'Date': days,
    'Minimum Temperature': min_temp,
    'Maximum Temperature': max_temp
})

df['Date'] = pd.to_datetime(df['Date'])


plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Minimum Temperature'], label='Minimum Temp', marker='o')
plt.plot(df['Date'], df['Maximum Temperature'], marker='o', label='Maximum Temp')

plt.xlabel("Date Time")
plt.ylabel("Temperature C")
plt.title("Temperatures in Nablus throughout the week")
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()


if not os.path.exists('date'):
    os.makedirs('data', exist_ok=True)


plt.savefig('data/Nablus_weather_chart.png')
df.to_csv('data/Nablus_weather.csv', index=False)

