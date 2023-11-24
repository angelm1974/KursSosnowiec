import json

# Wczytanie danych z pliku
def read_data_from_file():
    try:
        with open("kolarze.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

# Zapis danych do pliku
def save_data_to_file(data):
    with open("kolarze.json", "w") as file:
        json.dump(data, file)