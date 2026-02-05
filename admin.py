import tkinter as tk

# Live game settings dictionary
game_settings = {
    "gravity": 0.8,
    "jump_strength": 15,
    "player_speed": 5,
    "enable_powerups": True
}

# --- Admin actions ---
def kick_player():
    player_name = kick_entry.get()
    if player_name:
        print(f"[ADMIN] Kicked player: {player_name}")
        kick_entry.delete(0, tk.END)

def toggle_powerups():
    game_settings["enable_powerups"] = not game_settings["enable_powerups"]
    status_label.config(text=f"Power-ups enabled: {game_settings['enable_powerups']}")

# --- GUI setup ---
root = tk.Tk()
root.title("Admin Panel")
root.geometry("350x300")  # Bigger, nicer Windows-style window
root.resizable(True, True)

# Gravity control
tk.Label(root, text="Gravity:").pack()
gravity_var = tk.DoubleVar(value=game_settings["gravity"])
tk.Scale(root, from_=0, to=5, resolution=0.1, orient=tk.HORIZONTAL, variable=gravity_var).pack()

# Jump strength control
tk.Label(root, text="Jump Strength:").pack()
jump_var = tk.DoubleVar(value=game_settings["jump_strength"])
tk.Scale(root, from_=5, to=30, resolution=1, orient=tk.HORIZONTAL, variable=jump_var).pack()

# Player speed control
tk.Label(root, text="Player Speed:").pack()
speed_var = tk.DoubleVar(value=game_settings["player_speed"])
tk.Scale(root, from_=1, to=20, resolution=0.5, orient=tk.HORIZONTAL, variable=speed_var).pack()

# Kick player entry
tk.Label(root, text="Kick Player:").pack()
kick_entry = tk.Entry(root)
kick_entry.pack()
tk.Button(root, text="Kick", command=kick_player).pack()

# Toggle power-ups
tk.Button(root, text="Toggle Power-ups", command=toggle_powerups).pack()
status_label = tk.Label(root, text=f"Power-ups enabled: {game_settings['enable_powerups']}")
status_label.pack()

# --- Update settings live ---
def update_settings():
    game_settings["gravity"] = gravity_var.get()
    game_settings["jump_strength"] = jump_var.get()
    game_settings["player_speed"] = speed_var.get()
    root.after(100, update_settings)

update_settings()
root.mainloop()
