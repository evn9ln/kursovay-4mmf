import numpy as np
import matplotlib.pyplot as plt


def Uz(c_entry, const_k_entry, betta_entry, l_entry, R_entry, alpha_entry, T_entry, U0_entry, I_entry, K_entry):
    c = float(c_entry.get())
    const_k = float(const_k_entry.get())
    betta = float(betta_entry.get())
    l = float(l_entry.get())
    R = float(R_entry.get())
    alpha = float(alpha_entry.get())
    T = float(T_entry.get())
    U0 = float(U0_entry.get())

    I = int(I_entry.get())
    K = int(K_entry.get())

    ht = T / K
    hz = l / I

    integral = 1.2 * betta

    lower_layer = np.zeros(I+1)
    z_array = np.zeros(I + 1)  # создаем массив значений на координате z
    for ind in range(I + 1):
        z_array[ind] = ind * hz  # заполняем массив значениями
        lower_layer[ind] = U0

    for k in range(1, K+1):  # проходим по каждому слою наверх
        upper_layer = np.zeros(I + 1)  # массив для вернего слоя слоя

        temp = lower_layer[1] - 2 * hz * alpha * (lower_layer[0] - U0) / const_k
        upper_layer[0] = ht * (const_k * (lower_layer[1] - 2 * lower_layer[0] + temp) / hz ** 2 + integral) / c + \
                         lower_layer[0]

        for i in range(1, I):  # вычисляем значения в узлах верхнего слоя по основному уравнению при i от 1 до I-1
            temp = const_k * (lower_layer[i + 1] - 2 * lower_layer[i] + lower_layer[i - 1]) / hz ** 2 + integral
            temp = ht * temp / c + lower_layer[i]
            upper_layer[i] = temp

        temp = -2 * hz * alpha * (lower_layer[I] - U0) / const_k + lower_layer[I - 1]
        upper_layer[I] = ht * (const_k * (temp - 2 * lower_layer[I] + lower_layer[I - 1]) / hz ** 2 + integral) / c + \
                         lower_layer[I]

        # копируем слои
        lower_layer = upper_layer
      #  print(str(k / K * 100) + "%")

    # построение графика
    plt.xlabel("z")
    plt.ylabel("V")
    plt.plot(z_array, lower_layer, label="Явная схема при T=" + str(T))
    plt.title("Явная схема")
    plt.legend()
    plt.show()


def Ut(c_entry, const_k_entry, betta_entry, l_entry, R_entry, alpha_entry, T_entry, U0_entry, I_entry, K_entry,
       z_entry):
    c = float(c_entry.get())
    const_k = float(const_k_entry.get())
    betta = float(betta_entry.get())
    l = float(l_entry.get())
    R = float(R_entry.get())
    alpha = float(alpha_entry.get())
    T = float(T_entry.get())
    U0 = float(U0_entry.get())

    I = int(I_entry.get())
    K = int(K_entry.get())
    z = float(z_entry.get())

    ht = T / K
    hz = l / I

    t_array = np.zeros(K + 1)
    for ind in range(K + 1):
        t_array[ind] = ind * ht

    lower_layer = np.zeros(I + 1)
    for ind in range(I + 1):
        lower_layer[ind] = U0

    integral = 1.2 * betta
    number = int(z/hz)  # ищем номер узла, которые ближе всего к нужной координате z

    U = np.zeros(K + 1)  # создаем массив результата
    U[0] = lower_layer[number]

    for k in range(1, K+1):
        upper_layer = np.zeros(I + 1)  # массив для вернего слоя слоя

        temp = lower_layer[1] - 2 * hz * alpha * (lower_layer[0] - U0) / const_k
        upper_layer[0] = ht * (const_k * (lower_layer[1] - 2 * lower_layer[0] + temp) / hz ** 2 + integral) / c + \
                         lower_layer[0]

        for i in range(1, I):  # вычисляем значения в узлах верхнего слоя по основному уравнению при i от 1 до I-1
            temp = const_k * (lower_layer[i + 1] - 2 * lower_layer[i] + lower_layer[i - 1]) / hz ** 2 + integral
            temp = ht * temp / c + lower_layer[i]
            upper_layer[i] = temp

        temp = -2 * hz * alpha * (lower_layer[I] - U0) / const_k + lower_layer[I - 1]
        upper_layer[I] = ht * (const_k * (temp - 2 * lower_layer[I] + lower_layer[I - 1]) / hz ** 2 + integral) / c + \
                         lower_layer[I]

        # копируем слои
        lower_layer = upper_layer
        U[k] = lower_layer[number]
       # print(str(k / K * 100) + "%")

    plt.xlabel("t")
    plt.ylabel("V")
    plt.plot(t_array, U, label="Явная схема, I= " + str(I) + ",K=" + str(K))
    plt.title("Явная схема")
    plt.legend()
    plt.show()
