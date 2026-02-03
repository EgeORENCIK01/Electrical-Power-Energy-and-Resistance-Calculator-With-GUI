# Power   P = V*I
# Resistance   R = V/I
# Energy   E = P*T

# Importin Pythons GUI library
import tkinter as tk
from sys import exec_prefix
from tkinter import messagebox
from unittest import expectedFailure


# Calculation Functions
#Power Calculator
def power_cacl(voltage_entry,current_entry,result_label):
    try:
        v = float(voltage_entry.get())
        i = float(current_entry.get())
        power = v * i
        result_label.config(text = f"Power: {power:.2f} W")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
#Resistance Calculator
def resistance_calc(voltage_entry,current_entry,result_label):
    try:
        v = float(voltage_entry.get())
        i = float(current_entry.get())
        if i == 0:
            raise ZeroDivisionError
        resistance = v / i
        result_label.config(text = f"Resistance: {resistance:.2f} Ω")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Please enter a valid number.")
#Energy Calculator
def energy_calc(power_entry,time_entry,result_label):
    try:
        p = float(power_entry.get())
        t = float(time_entry.get())
        energy = p * t
        result_label.config(text = f"Energy: {energy:.2f} J")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

#GUI Part
root = tk.Tk()
root.title("Power,Resistance,Energy Calculator")
root.geometry("350x350")

tk.Label(root, text="Voltage (V):").pack()
voltage_entry = tk.Entry(root)
voltage_entry.pack()

tk.Label(root, text="Current (A):").pack()
current_entry = tk.Entry(root)
current_entry.pack()

tk.Label(root, text="Power (W):").pack()
power_entry = tk.Entry(root)
power_entry.pack()

tk.Label(root, text="Time (s):").pack()
time_entry = tk.Entry(root)
time_entry.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack(pady=15)

tk.Button(root,
          text="Calculate Power",
          command=lambda:
          power_cacl(voltage_entry, current_entry, result_label)).pack(pady=5)

tk.Button(root,
          text="Calculate Resistance",
          command=lambda:
          resistance_calc(voltage_entry, current_entry, result_label)).pack(pady=5)

tk.Button(root,
          text="Calculate Energy",
          command=lambda:
          energy_calc(power_entry, time_entry, result_label)).pack(pady=5)

root.mainloop()