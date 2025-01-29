import requests
import tkinter as tk
from tkinter import Toplevel, Label
from tkinter import messagebox

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(data):
    if data:
        weather_info = (f"City: {data['name']}, {data['sys']['country']}\n"
                        f"Temperature: {data['main']['temp']}°C\n"
                        f"Feels Like: {data['main']['feels_like']}°C\n"
                        f"Min Temperature: {data['main']['temp_min']}°C\n"
                        f"Max Temperature: {data['main']['temp_max']}°C\n"
                        f"Humidity: {data['main']['humidity']}%\n"
                        f"Pressure: {data['main']['pressure']} hPa\n"
                        f"Wind Speed: {data['wind']['speed']} m/s\n"
                        f"Wind Direction: {data['wind']['deg']}°\n"
                        f"Cloudiness: {data['clouds']['all']}%\n"
                        f"Weather: {data['weather'][0]['description'].title()}")
        
        popup = Toplevel(root)
        popup.title("Weather Information")
        popup.geometry("400x300")
        popup.configure(bg="#1e3c72")  # Gradient-like background color
        
        Label(popup, text=weather_info, font=("Arial", 12), bg="#1e3c72", fg="white", justify="left").pack(pady=20, padx=20)
    else:
        messagebox.showerror("Error", "Weather data not found.")

def fetch_weather():
    city = city_entry.get()
    api_key = "491fcd1cc87ad1478baf74231c07dfb3"  # Replace with your OpenWeatherMap API key
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)

# GUI Setup
root = tk.Tk()
root.title("Weather Analyzer")

tk.Label(root, text="Enter city name:").pack(pady=5)
city_entry = tk.Entry(root, width=30)  # Increased input box size
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=fetch_weather).pack(pady=10)

root.mainloop()