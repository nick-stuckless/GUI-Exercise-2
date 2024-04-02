"""
Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
from tkinter import ttk, Tk, PhotoImage
import os
import ctypes
import poke_api

# Get the script and images directory
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist
if not os.path.isdir(images_dir):
    os.makedirs(images_dir)

# Create the main window
root = Tk()
root.title("Pokemon Viewer")
root.minsize(width=500, height=600)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# TODO: Set the icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Pokemon.Viewer")
root.iconbitmap(os.path.join(script_dir, "poke_ball.ico")) 

# TODO: Create frames
frame = ttk.Frame(root)
frame.grid(sticky="nsew")
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# TODO: Populate frames with widgets and define event handler functions
image_path = os.path.join(script_dir, "poke_ball.png")
photo = PhotoImage(file=image_path)
img_label = ttk.Label(frame, image=photo)
img_label.grid(row=0, column=0, padx=10, pady=10)

poke_names = poke_api.get_pokemon_names()
if not poke_names:
    poke_names = []
poke_cbox = ttk.Combobox(frame, values=poke_names, state="readonly")
poke_cbox.set("Select a pokemon")
poke_cbox.grid(row=1, column=0, padx=10, pady=10)

def select_pokemon(event):
    pokemon = poke_cbox.get()
    image_path = poke_api.get_pokemon_art(pokemon, images_dir)
    if image_path:
        photo["file"] = image_path
        img_label["image"] = photo
        img_label["text"] = ""
        #reenable button
    else:
        img_label["text"] = "No artwork available"
        img_label["image"] = None
        pass

poke_cbox.bind("<<ComboboxSelected>>", select_pokemon)
    

root.mainloop()