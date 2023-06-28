import tkinter as tk
import v
import s
import k

def run_volume_control():
    v.run_volume_control()

def run_brightness_control():
    s.run_brightness_control()

def run_keyboard_input():
    k.run_keyboard_input()

def close_window():
    root.destroy()

root = tk.Tk()
root.title("HAND GESTURE SYSTEM CONTROL")

# Create the buttons
vol_button = tk.Button(root, command=run_volume_control)
vol_image = tk.PhotoImage(file="vol.png")
vol_button.config(image=vol_image)
vol_button.pack(side=tk.LEFT)

sbc_button = tk.Button(root, command=run_brightness_control)
sbc_image = tk.PhotoImage(file="sbc.png")
sbc_button.config(image=sbc_image)
sbc_button.pack(side=tk.LEFT)

key_button = tk.Button(root, command=run_keyboard_input)
key_image = tk.PhotoImage(file="key.png")
key_button.config(image=key_image)
key_button.pack(side=tk.LEFT)

q_button = tk.Button(root, text="Quit", command=close_window)
q_button.pack(side=tk.RIGHT)

root.mainloop()
