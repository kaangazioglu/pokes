
import tkinter as tk
from tkinter import *
import requests as requests




def get_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon"
    pokemon_name = entry.get()

    response = requests.get(f"{url}/{pokemon_name}")

    if response.status_code == 200:
        pokemon_data = response.json()

        name_label.config(text="Name: " + pokemon_data["name"])
        weight_label.config(text="Weight: " + str(pokemon_data["weight"]))
        height_label.config(text="Height: " + str(pokemon_data["height"]))
        abilities = [ability["ability"]["name"] for ability in pokemon_data["abilities"]]
        abilities_label.config(text="Abilities: " + ", ".join(abilities))
    else:
        name_label.config(text="Failed to retrieve Pokemon data")

window = tk.Tk()
window.title("Pokédex")
window.minsize(width=500, height=700)

photo = tk.PhotoImage(file=r"as.png")
label_image = Label(image=photo)
label_image.pack()

label = tk.Label(text="Enter a Pokémon name:")
label.pack(pady=10)

entry = tk.Entry()
entry.pack(pady=5)

button = tk.Button(text="Get Pokémon Data", command=get_pokemon)
button.pack(pady=5)

name_label = tk.Label(text="")
name_label.pack(pady=5)

weight_label = tk.Label(text="")
weight_label.pack(pady=5)

height_label = tk.Label(text="")
height_label.pack(pady=5)

abilities_label = tk.Label(text="")
abilities_label.pack(pady=5)

window.mainloop()