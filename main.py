import tkinter as tk
from tkinter.ttk import Combobox
import explict_
import implicit

method = ["Явная", "Неявная"]
dependence = ["U от t", "U от z"]


def disableEntry(entry):
    entry.config(state='disable')


def allowEntry(entry):
    entry.config(state='normal')


def dependenceChanged(event):
    if dependence_combo.get() == "U от z":
        disableEntry(z_entry)
    else:
        allowEntry(z_entry)


def buildGraph():
    if dependence_combo.get() == "..." or method_combo.get() == "...":
        return
    if method_combo.get() == "Явная":
        if dependence_combo.get() == "U от z":
            explict_.Uz(c_entry, const_k_entry, betta_entry, l_entry, R_entry, alpha_entry, T_entry, U0_entry, I_entry, K_entry)
        elif dependence_combo.get() == "U от t":
            explict_.Ut(c_entry, const_k_entry, betta_entry, l_entry, R_entry, alpha_entry, T_entry, U0_entry, I_entry, K_entry, z_entry)
    elif method_combo.get() == "Неявная":
        if dependence_combo.get() == "U от z":
            implicit.Uz(c_entry, const_k_entry, betta_entry, l_entry, R_entry, alpha_entry, T_entry, U0_entry, I_entry, K_entry)
        elif dependence_combo.get() == "U от t":
            implicit.Ut(c_entry, const_k_entry, betta_entry, l_entry, R_entry, alpha_entry, T_entry, U0_entry, I_entry, K_entry, z_entry)


root = tk.Tk()
root.title("Построение графиков разностных схем")
root.geometry('300x400')

method_label = tk.Label(root, text="Cхема")
method_combo = Combobox(root, values=method)
method_combo.set("...")
method_combo['state'] = 'readonly'

method_label.grid(row=1, column=2)
method_combo.grid(row=1, column=3)

dependence_label = tk.Label(root, text="Зависимость")
dependence_combo = Combobox(root, values=dependence)
dependence_combo.set("...")
dependence_combo['state'] = 'readonly'
dependence_combo.bind('<<ComboboxSelected>>', dependenceChanged)

dependence_label.grid(row=2, column=2)
dependence_combo.grid(row=2, column=3)

# для c
c_label = tk.Label(root, text="c")
c_entry = tk.Entry(root)
c_entry.insert(0, "2")

c_label.grid(row=3, column=2)
c_entry.grid(row=3, column=3)

# для const_k
const_k_label = tk.Label(root, text="const_k")
const_k_entry = tk.Entry(root)
const_k_entry.insert(0, "0.12")

const_k_label.grid(row=4, column=2)
const_k_entry.grid(row=4, column=3)

# для betta
betta_label = tk.Label(root, text="betta")
betta_entry = tk.Entry(root)
betta_entry.insert(0, "0.13")

betta_label.grid(row=5, column=2)
betta_entry.grid(row=5, column=3)

# для l
l_label = tk.Label(root, text="l")
l_entry = tk.Entry(root)
l_entry.insert(0, "11")

l_label.grid(row=6, column=2)
l_entry.grid(row=6, column=3)

# для R
R_label = tk.Label(root, text="R")
R_entry = tk.Entry(root)
R_entry.insert(0, "1")

R_label.grid(row=7, column=2)
R_entry.grid(row=7, column=3)

# для alpha
alpha_label = tk.Label(root, text="alpha")
alpha_entry = tk.Entry(root)
alpha_entry.insert(0, "0.002")

alpha_label.grid(row=8, column=2)
alpha_entry.grid(row=8, column=3)

# для T
T_label = tk.Label(root, text="T")
T_entry = tk.Entry(root)
T_entry.insert(0, "30")

T_label.grid(row=9, column=2)
T_entry.grid(row=9, column=3)

# для U0
U0_label = tk.Label(root, text="U0")
U0_entry = tk.Entry(root)
U0_entry.insert(0, "0")

U0_label.grid(row=10, column=2)
U0_entry.grid(row=10, column=3)

# конкретная точка по z
z_label = tk.Label(root, text="z")
z_entry = tk.Entry(root)
z_entry.insert(0, "0.0")

z_label.grid(row=11, column=2)
z_entry.grid(row=11, column=3)

# кол-во узлов по длине
I_label = tk.Label(root, text="I")
I_entry = tk.Entry(root)
I_entry.insert(0, "100")

I_label.grid(row=12, column=2)
I_entry.grid(row=12, column=3)

# кол-во узлов по времени
K_label = tk.Label(root, text="K")
K_entry = tk.Entry(root)
K_entry.insert(0, "10000")

K_label.grid(row=13, column=2)
K_entry.grid(row=13, column=3)

graph_btn = tk.Button(root, text="Построить график", command=buildGraph)
graph_btn.grid(row=14, column=3)

root.mainloop()
