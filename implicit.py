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

    ht = T / K /4
    hz = l / I

    integral = 1.2 * betta

    layer = np.zeros(I+1)
    z_array = np.zeros(I + 1)  # создаем массив значений на координате z
    for ind in range(I + 1):
        z_array[ind] = ind * hz  # заполняем массив значениями
        layer[ind] = U0

    A0 = -2 * const_k / hz**2
    B0 = c / ht + 2 * const_k / hz**2 + 2 * alpha / hz
    Ai = - const_k / hz**2
    Bi = c / ht + 2 * const_k / hz**2
    Ci = -const_k / hz ** 2
    BI = c / ht + 2 * const_k / hz ** 2 + 2 * alpha / hz
    CI = -2 * const_k / hz ** 2

    for k in range(1, K+1):  # проходим по каждому слою наверх
        D = np.zeros(I+1)
        D[0] = integral + c * layer[0] / ht + 2 * alpha * U0 / hz
        for i in range(1, I):
            D[i] = integral + c * layer[i] / ht
        D[I] = integral + c * layer[I] / ht + 2 * alpha * U0 / hz

        alphas = np.zeros(I)
        betas = np.zeros(I)

        alphas[0] = -A0 / B0
        betas[0] = D[0] / B0

        for i in range(1, I):
            alphas[i] = -Ai / (Bi + Ci * alphas[i - 1])
            betas[i] = (D[i] - Ci * betas[i - 1]) / (Bi + Ci * alphas[i - 1])

        layer[I] = (D[I] - CI * betas[I - 1]) / (BI + CI * alphas[I - 1])
        for i in range(I - 1, -1, -1):
            layer[i] = alphas[i] * layer[i + 1] + betas[i]

       # print(str(k / K * 100) + "%")

    # построение графика
    plt.xlabel("z")
    plt.ylabel("V")
    plt.plot(z_array, layer, label="Неявная схема при T=" + str(T))
    print(layer)
    plt.title("Неявная схема")
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

    layer = np.zeros(I + 1)
    for ind in range(I + 1):
        layer[ind] = U0

    integral = 1.2 * betta
    number = int(z/hz)  # ищем номер узла, которые ближе всего к нужной координате z

    U = np.zeros(K + 1)  # создаем массив результата
    U[0] = layer[number]

    A0 = -2 * const_k / hz ** 2
    B0 = c / ht + 2 * const_k / hz ** 2 + 2 * alpha / hz
    Ai = - const_k / hz ** 2
    Bi = c / ht + 2 * const_k / hz ** 2
    Ci = -const_k / hz ** 2
    BI = c / ht + 2 * const_k / hz ** 2 + 2 * alpha / hz
    CI = -2 * const_k / hz ** 2

    for k in range(1, K + 1):  # проходим по каждому слою наверх
        D = np.zeros(I + 1)
        D[0] = integral + c * layer[0] / ht + 2 * alpha * U0 / hz
        for i in range(1, I):
            D[i] = integral + c * layer[i] / ht
        D[I] = integral + c * layer[I] / ht + 2 * alpha * U0 / hz

        alphas = np.zeros(I)
        betas = np.zeros(I)

        alphas[0] = -A0 / B0
        betas[0] = D[0] / B0

        for i in range(1, I):
            alphas[i] = -Ai / (Bi + Ci * alphas[i - 1])
            betas[i] = (D[i] - Ci * betas[i - 1]) / (Bi + Ci * alphas[i - 1])

        layer[I] = (D[I] - CI * betas[I - 1]) / (BI + CI * alphas[I - 1])
        for i in range(I - 1, -1, -1):
            layer[i] = alphas[i] * layer[i + 1] + betas[i]

        U[k] = layer[number]
       # print(str(k / K * 100) + "%")

    plt.xlabel("t")
    plt.ylabel("V")
    plt.plot(t_array, U, label="Неявная схема, I= " + str(I) + ",K=" + str(K))
    plt.title("Неявная схема")
    plt.legend()
    plt.show()
