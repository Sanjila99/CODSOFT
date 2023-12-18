import secrets
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

repeat = 0

def generate_password():
    global repeat
    try:
        repeat = int(repeat_entry.get())
        length = int(length_entry.get())
    except:
        messagebox.showerror(message="Please enter valid numeric values for length and repetition")
        return

    character_string = get_character_set()
    password = ''.join(secrets.choice(character_string) for _ in range(length))

    password_v.set("Created password:" + str(password))
    update_strength_meter(password)

def get_character_set():
    character_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[{]}|;:'\",<.>/?`~"
    return character_set

def copy_to_clipboard():
    password = password_v.get().split(":")[1]
    password_gen.clipboard_clear()
    password_gen.clipboard_append(password)
    password_gen.update()

def update_strength_meter(password):
    strength = calculate_strength(password)
    strength_meter_value.set(str(strength))

def calculate_strength(password):
    return len(set(password))

def create_rounded_button(root, text, command, x, y):
    rounded_button = ttk.Button(root, text=text, command=command, style="Rounded.TButton")
    rounded_button.place(x=x, y=y)
    return rounded_button

# Tkinter Window Setup
password_gen = Tk()
password_gen.geometry("600x300")
password_gen.title("Password Generator")

# Customized colors and fonts
bg_color = "#f0f0f0"
button_color = "#FFC0CB"
button_text_color = "black"
label_font = ('Helvetica', 12)
button_font = ('Helvetica', 10, 'bold')

# Configure the window background color
password_gen.configure(bg=bg_color)

# Style for rounded buttons
style = ttk.Style()
style.configure("Rounded.TButton", foreground=button_text_color, background=button_color, font=button_font)

# Title Label
title_label = Label(password_gen, text="Strong Password Generator", font=('Helvetica', 14, 'bold'), bg=bg_color)
title_label.pack(pady=10)

# Length Input
length_label = Label(password_gen, text="Enter length of password: ", font=label_font, bg=bg_color)
length_label.place(x=20, y=50)
length_entry = Entry(password_gen, width=3)
length_entry.place(x=200, y=50)

# Read repetition
repeat_label = Label(password_gen, text="Repetition? 1: no repetition, 2: otherwise:", font=label_font, bg=bg_color)
repeat_label.place(x=20, y=80)
repeat_entry = Entry(password_gen, width=3)
repeat_entry.place(x=310, y=80)

# Generate password with style
generate_button = create_rounded_button(password_gen, "Generate Strong Password", generate_password, 80, 120)

# Display password
password_v = StringVar()
password_label = Label(password_gen, bd=0, bg="#d9d9d9", textvariable=password_v, font=label_font)
password_label.place(x=20, y=150, height=30, width=560)

# Copy to clipboard button
copy_button = create_rounded_button(password_gen, "Copy to Clipboard", copy_to_clipboard, 80, 210)

# Strength meter
strength_meter_label = Label(password_gen, text="Strength Meter:", font=label_font, bg=bg_color)
strength_meter_label.place(x=20, y=240)

strength_meter_value = StringVar()
strength_meter_display = Label(password_gen, bd=0, bg="#d9d9d9", textvariable=strength_meter_value, font=label_font)
strength_meter_display.place(x=150, y=245, height=30, width=240)

# Run the Tkinter event loop
password_gen.mainloop()
