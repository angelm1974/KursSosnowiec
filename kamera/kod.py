import requests

api_key = "ca7658ae17cd2320d08b93edcb767a0a"

# Podmień na szerokość i długość geograficzną lokalizacji
lat = 37.7749
lon = -122.4194
city_name = "Kraków"

# Podstawowy URL do API OpenWeatherMap
# dla szerokości i długości geograficznej
# base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
# dla nazwy miasta
base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

# Wysyłanie żądania GET do API
response = requests.get(base_url)

# Sprawdzanie kodu statusu odpowiedzi
if response.status_code == 200:
    # Wydobycie danych pogodowych z odpowiedzi JSON
    weather_data = response.json()
    print(weather_data)
    # Tutaj możesz dodać swój kod do wykorzystania danych pogodowych
else:
    # Obsługa różnych kodów odpowiedzi
    print(f"Błąd: Nie można pobrać danych. Kod statusu HTTP: {response.status_code}")

# Tutaj możesz dodać dodatkowe obsługi błędów, jeśli jest to konieczne
