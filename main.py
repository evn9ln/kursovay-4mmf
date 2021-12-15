# Интерфейсная часть

import tkinter as tk
from tkinter.ttk import Combobox
import explict_
import implicit

method = ["Явная", "Неявная"]
dependence = ["V от t", "V от z"]

# функции для определения введены ли новые параметры
def disableEntry(entry):
    entry.config(state='disable')


def allowEntry(entry):
    entry.config(state='normal')


def dependenceChanged(event):
    if dependence_combo.get() == "V от z":
        disableEntry(z_entry)
    else:
        allowEntry(z_entry)

# построение графиков
def buildGraph():
    # если не выбрана зависимость или схема, то ничего не делаем
    if dependence_combo.get() == "..." or method_combo.get() == "...":
        return
    if method_combo.get() == "Явная":
        if dependence_combo.get() == "V от z":
            explict_.Vz(c_entry, const_k_entry, betta_entry, l_entry, R_entry, alpha_entry, T_entry, U0_entry, I_entry, K_entry)
        elif dependence_combo.get() == "V от t":
            explict_.Vt(c_entry, const_k_entry, betta_entry, l_entry, R_entry, alpha_entry, T_entry, U0_entry, I_entry, K_entry, z_entry)
    elif method_combo.get() == "Неявная":
        if dependence_combo.get() == "V от z":
            implicit.Vz(c_entry, const_k_entry, betta_entry, l_entry, R_entry, alpha_entry, T_entry, U0_entry, I_entry, K_entry)
        elif dependence_combo.get() == "V от t":
            implicit.Vt(c_entry, const_k_entry, betta_entry, l_entry, R_entry, alpha_entry, T_entry, U0_entry, I_entry, K_entry, z_entry)

# создаем окошко интерфейса
root = tk.Tk()
root.title("Построение графиков разностных схем")
root.geometry('300x400')

# выпадающее окно с выбором схемы
method_label = tk.Label(root, text="Cхема")
method_combo = Combobox(root, values=method)
method_combo.set("...")
method_combo['state'] = 'readonly'

# позиция
method_label.grid(row=1, column=2)
method_combo.grid(row=1, column=3)

# выпадающее окно с выбором зависимости
# V от t - распределение температуры тепла в диске в промежуток времени t
# V от z - изменение температуры в конкретной точке на всем временном промежутке
dependence_label = tk.Label(root, text="Зависимость")
dependence_combo = Combobox(root, values=dependence)
dependence_combo.set("...")
dependence_combo['state'] = 'readonly'
dependence_combo.bind('<<ComboboxSelected>>', dependenceChanged)

dependence_label.grid(row=2, column=2)
dependence_combo.grid(row=2, column=3)

# задание поля для c и инициализация стандартным значением
c_label = tk.Label(root, text="c")
c_entry = tk.Entry(root)
c_entry.insert(0, "2")

c_label.grid(row=3, column=2)
c_entry.grid(row=3, column=3)

# задание поля для k и инициализация стандартным значением
const_k_label = tk.Label(root, text="const_k")
const_k_entry = tk.Entry(root)
const_k_entry.insert(0, "0.12")

const_k_label.grid(row=4, column=2)
const_k_entry.grid(row=4, column=3)

# задание поля для betta и инициализация стандартным значением
betta_label = tk.Label(root, text="betta")
betta_entry = tk.Entry(root)
betta_entry.insert(0, "0.13")

betta_label.grid(row=5, column=2)
betta_entry.grid(row=5, column=3)

# задание поля для l и инициализация стандартным значением
l_label = tk.Label(root, text="l")
l_entry = tk.Entry(root)
l_entry.insert(0, "11")

l_label.grid(row=6, column=2)
l_entry.grid(row=6, column=3)

# задание поля для R и инициализация стандартным значением
R_label = tk.Label(root, text="R")
R_entry = tk.Entry(root)
R_entry.insert(0, "1")

R_label.grid(row=7, column=2)
R_entry.grid(row=7, column=3)

# задание поля для alpha и инициализация стандартным значением
alpha_label = tk.Label(root, text="alpha")
alpha_entry = tk.Entry(root)
alpha_entry.insert(0, "0.002")

alpha_label.grid(row=8, column=2)
alpha_entry.grid(row=8, column=3)

# задание поля для T и инициализация стандартным значением
T_label = tk.Label(root, text="T")
T_entry = tk.Entry(root)
T_entry.insert(0, "30")

T_label.grid(row=9, column=2)
T_entry.grid(row=9, column=3)

# задание поля для u_0 и инициализация стандартным значением
U0_label = tk.Label(root, text="U0")
U0_entry = tk.Entry(root)
U0_entry.insert(0, "0")

U0_label.grid(row=10, column=2)
U0_entry.grid(row=10, column=3)

# задание поля для z и инициализация стандартным значением (в данном случае просто 0)
z_label = tk.Label(root, text="z")
z_entry = tk.Entry(root)
z_entry.insert(0, "0.0")

z_label.grid(row=11, column=2)
z_entry.grid(row=11, column=3)

# задание поля для количества пространственных узлов
# и инициализация стандартным значением (было выбрано 100)
I_label = tk.Label(root, text="I")
I_entry = tk.Entry(root)
I_entry.insert(0, "100")

I_label.grid(row=12, column=2)
I_entry.grid(row=12, column=3)

# задание поля для количества временных узлов
# и инициализация стандартным значением (было выбрано 10000)
# для явной схемы необходимо такое значение, если задать 100, то будет неустойчива
K_label = tk.Label(root, text="K")
K_entry = tk.Entry(root)
K_entry.insert(0, "10000")

K_label.grid(row=13, column=2)
K_entry.grid(row=13, column=3)

# задание кнопки для запуска функции по построению графиков
graph_btn = tk.Button(root, text="Построить график", command=buildGraph)
graph_btn.grid(row=14, column=3)

# все делаем в бесконечном цикле пока вручную не закроется окно
root.mainloop()
