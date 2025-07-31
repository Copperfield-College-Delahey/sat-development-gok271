import tkinter as tk
from tkinter import ttk

# Root window
root = tk.Tk()
root.title("MoodMeal")
root.geometry("900x600")
root.config(bg="#fefefe")

# Sidebar
sidebar = tk.Frame(root, bg="#e6ded5", width=150)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Sidear buttons
for text in ["home", "Favourites", "About", "Recipes", "Contact"]:
       tk.Button(sidebar, text=text, bg="#e6ded5", fg="black", relief="flat", anchor="w", padx=20).pack(fill=tk.X, pady=5)

# Main Frame
main = tk.Frame(root, bg="#f9f1e7")
main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Title
tittle = tk.Label(main, text="How are you feeling?", font=("Arial", 20, "bold"), bg='#f9f1e')
tittle.pack(anchor='nw')

# Mood buttons
moods = ["Happy", "Relaxed", "Sad", "Inspired", "Amazed", "Tired", "Optimistic", "Stressed", "Excited"]
mood_frame = tk.Frame(main, bg="#f9f1e7")
mood_frame.pack(anchor="nw", pady=10)

for i, mood in enumerate(moods):
       btn = tk.Button