from logging import info
import tkinter as tk
import requests

def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }
def pkm():
    pkm = tk.Tk()
    pkm.title("Pokemon Info")
    pkm.geometry("400x300")
    
    entry = tk.Entry(pkm, width=30)
    entry.pack(pady=10)

    name_label = tk.Label(pkm, text=f"Name: ")
    name_label.pack(pady=5)
    height_label = tk.Label(pkm, text=f"Height: ")
    height_label.pack(pady=5)
    weight_label = tk.Label(pkm, text="Weight: ")
    weight_label.pack(pady=5)
    types_label = tk.Label(pkm, text="Types: ")
    types_label.pack(pady=5)

    def fetch_info():
        poke_name = entry.get()
        info = getPoke(poke_name)
        if info:
            name_label.config(text=f"Name: {info['name']}")
            height_label.config(text=f"Height: {info['height']}")
            weight_label.config(text=f"Weight: {info['weight']}")
            types_label.config(text=f"Types: {', '.join(info['types'])}")
        else:
            print("Pokemon not found.")
    fetch_button = tk.Button(pkm, text="Fetch Info", command=fetch_info)
    fetch_button.pack(pady=10)

    pkm.mainloop()
pkm()