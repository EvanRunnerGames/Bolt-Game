import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main window
window = tk.Tk()
window.iconbitmap("media/icon.png")
window.title("Project Bolt")

# Create a label
label = tk.Label(window, text="Hello, Tkinter!")
label.pack(pady=10)

# Create a button
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Run the main loop
window.mainloop()
