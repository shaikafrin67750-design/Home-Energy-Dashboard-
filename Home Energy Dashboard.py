import tkinter as tk
from tkinter import messagebox

# Appliance data
appliances = {
    "Fan": {"power": 75, "hours": 6},
    "Light": {"power": 20, "hours": 5},
    "TV": {"power": 100, "hours": 4},
    "Refrigerator": {"power": 150, "hours": 10}
}

# Calculate energy consumption
def calculate_energy():
    total_energy = 0

    for appliance, data in appliances.items():
        energy = (data["power"] * data["hours"]) / 1000
        total_energy += energy

    result_label.config(
        text=f"Total Daily Energy: {total_energy:.2f} kWh"
    )

    monthly_energy = total_energy * 30

    monthly_label.config(
        text=f"Estimated Monthly Energy: {monthly_energy:.2f} kWh"
    )


# Add appliance
def add_appliance():
    name = name_entry.get()
    power = power_entry.get()
    hours = hours_entry.get()

    if name == "" or power == "" or hours == "":
        messagebox.showwarning("Warning", "Please enter all details.")
        return

    try:
        power = float(power)
        hours = float(hours)

        appliances[name] = {
            "power": power,
            "hours": hours
        }

        messagebox.showinfo(
            "Success",
            f"{name} added successfully!"
        )

        name_entry.delete(0, tk.END)
        power_entry.delete(0, tk.END)
        hours_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Power and hours must be numbers."
        )


# Create window
root = tk.Tk()
root.title("Home Energy Dashboard")
root.geometry("600x600")
root.configure(bg="black")

# Title
title = tk.Label(
    root,
    text="HOME ENERGY DASHBOARD",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="black"
)
title.pack(pady=20)

# Input frame
frame = tk.Frame(root, bg="black")
frame.pack(pady=10)

# Appliance name
tk.Label(
    frame,
    text="Appliance Name:",
    fg="white",
    bg="black",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10, pady=10)

name_entry = tk.Entry(frame, width=25)
name_entry.grid(row=0, column=1)

# Power
tk.Label(
    frame,
    text="Power (Watts):",
    fg="white",
    bg="black",
    font=("Arial", 12)
).grid(row=1, column=0, padx=10, pady=10)

power_entry = tk.Entry(frame, width=25)
power_entry.grid(row=1, column=1)

# Hours
tk.Label(
    frame,
    text="Usage Hours/Day:",
    fg="white",
    bg="black",
    font=("Arial", 12)
).grid(row=2, column=0, padx=10, pady=10)

hours_entry = tk.Entry(frame, width=25)
hours_entry.grid(row=2, column=1)

# Add button
add_button = tk.Button(
    root,
    text="Add Appliance",
    command=add_appliance,
    font=("Arial", 12, "bold")
)
add_button.pack(pady=10)

# Calculate button
calculate_button = tk.Button(
    root,
    text="Calculate Energy",
    command=calculate_energy,
    font=("Arial", 14, "bold")
)
calculate_button.pack(pady=15)

# Results
result_label = tk.Label(
    root,
    text="Total Daily Energy: 0 kWh",
    font=("Arial", 18),
    fg="white",
    bg="black"
)
result_label.pack(pady=10)

monthly_label = tk.Label(
    root,
    text="Estimated Monthly Energy: 0 kWh",
    font=("Arial", 18),
    fg="white",
    bg="black"
)
monthly_label.pack(pady=10)

# Start application
root.mainloop()
