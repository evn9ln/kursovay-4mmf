# Код для неявной схемы

import numpy as np
import matplotlib.pyplot as plt

# функция для зависимости V_z
# изменение температуры в конкретной точке на всем временном промежутке
# принимает в параметры значения всех полей
def Vz(c_entry, const_k_entry, betta_entry, l_entry, R_entry, alpha_entry, T_entry, U0_entry, I_entry, K_entry):
    # кастим к типу float (изначально строки)
    c = float(c_entry.get())
    const_k = float(const_k_entry.get())
    betta = float(betta_entry.get())
    l = float(l_entry.get())
    R = float(R_entry.get())
    alpha = float(alpha_entry.get())
    T = float(T_entry.get())
    U0 = float(U0_entry.get())

    # Число интервало разбиения кастим к инту
    I = int(I_entry.get())
    K = int(K_entry.get())

    # считаем шаги разбиения
    ht = T / K / 4
    hz = l / I

    # интеграл использующейся в схеме
    integral = 1.2 * betta

    layer = np.zeros(I+1) # создаем слой как массив размерности I+1
    z_array = np.zeros(I + 1)  # создаем массив значений на координате z

    # проводим дискретизацию по i
    for ind in range(I + 1):
        z_array[ind] = ind * hz  # заполняем массив значениями
        layer[ind] = U0

    # Определяем формулы для подсчета прогоночных коэффициентов
    A0 = -2 * const_k / hz**2
    B0 = c / ht + 2 * const_k / hz**2 + 2 * alpha / hz
    Ai = - const_k / hz**2
    Bi = c / ht + 2 * const_k / hz**2
    Ci = -const_k / hz ** 2
    BI = c / ht + 2 * const_k / hz ** 2 + 2 * alpha / hz
    CI = -2 * const_k / hz ** 2

    for k in range(1, K+1):  # проходим по каждому слою наверх
        # считаем нижний узел
        D = np.zeros(I+1)
        D[0] = integral + c * layer[0] / ht + 2 * alpha * U0 / hz

        # считаем нижний узел для каждого слоя
        for i in range(1, I):
            D[i] = integral + c * layer[i] / ht
        D[I] = integral + c * layer[I] / ht + 2 * alpha * U0 / hz

        # задаем массивы для значения коэффициентов использующихся
        # в рекуррентном прогоночном соотношении
        alphas = np.zeros(I)
        betas = np.zeros(I)

        # вычисляем значения коэффов в i=0
        alphas[0] = -A0 / B0
        betas[0] = D[0] / B0

        for i in range(1, I): # вычисляем значения коэффов в центральной части i от 1 до I
            alphas[i] = -Ai / (Bi + Ci * alphas[i - 1])
            betas[i] = (D[i] - Ci * betas[i - 1]) / (Bi + Ci * alphas[i - 1])

        # вычисляем последний слой
        layer[I] = (D[I] - CI * betas[I - 1]) / (BI + CI * alphas[I - 1])
        for i in range(I - 1, -1, -1): # считаем центральную часть слоя (от 1 до I-1)
            # вычисляем слои по рекуррентному прогочному соотношению
            layer[i] = alphas[i] * layer[i + 1] + betas[i]

       # print(str(k / K * 100) + "%")

    # построение графика по последнему слою по I
    plt.xlabel("z")
    plt.ylabel("V")
    plt.plot(z_array, layer, label="Неявная схема при T=" + str(T))
    print(layer)
    plt.title("Неявная схема")
    plt.legend()
    plt.show()


# функция для зависимости V_t
# распределение температуры тепла в диске в промежуток времени t
# принимает в параметры значения всех полей
def Vt(c_entry, const_k_entry, betta_entry, l_entry, R_entry, alpha_entry, T_entry, U0_entry, I_entry, K_entry,
       z_entry):
    # кастим к типу float (изначально строки)
    c = float(c_entry.get())
    const_k = float(const_k_entry.get())
    betta = float(betta_entry.get())
    l = float(l_entry.get())
    R = float(R_entry.get())
    alpha = float(alpha_entry.get())
    T = float(T_entry.get())
    U0 = float(U0_entry.get())
    z = float(z_entry.get())

    # Число интервало разбиения кастим к инту
    I = int(I_entry.get())
    K = int(K_entry.get())

    # считаем шаги разбиения
    ht = T / K
    hz = l / I

    # проводим дискретизацию по t
    t_array = np.zeros(K + 1)
    for ind in range(K + 1):
        t_array[ind] = ind * ht

    # задаем массив для слоя
    layer = np.zeros(I + 1)
    for ind in range(I + 1):
        layer[ind] = U0

    # вычисляем интеграл из схемы
    integral = 1.2 * betta

    # ищем номер узла, которые ближе всего к нужной координате z
    number = int(z/hz)

    # создаем массив результата
    V = np.zeros(K + 1)
    V[0] = layer[number]

    # Определяем формулы для подсчета прогоночных коэффициентов
    A0 = -2 * const_k / hz ** 2
    B0 = c / ht + 2 * const_k / hz ** 2 + 2 * alpha / hz
    Ai = - const_k / hz ** 2
    Bi = c / ht + 2 * const_k / hz ** 2
    Ci = -const_k / hz ** 2
    BI = c / ht + 2 * const_k / hz ** 2 + 2 * alpha / hz
    CI = -2 * const_k / hz ** 2

    for k in range(1, K + 1):  # проходим по каждому слою наверх
        D = np.zeros(I + 1)
        # считаем нижний узел
        D[0] = integral + c * layer[0] / ht + 2 * alpha * U0 / hz

        # считаем нижний узел для каждого слоя
        for i in range(1, I):
            D[i] = integral + c * layer[i] / ht

        # считаем нижний узел для последнего слоя (для обратного хода прогонки)
        D[I] = integral + c * layer[I] / ht + 2 * alpha * U0 / hz

        # задаем массивы для значения коэффициентов использующихся
        # в рекуррентном прогоночном соотношении
        alphas = np.zeros(I)
        betas = np.zeros(I)

        # вычисляем значения коэффов в i=0
        alphas[0] = -A0 / B0
        betas[0] = D[0] / B0

        # вычисляем значения коэффов в центральной части i от 1 до I
        for i in range(1, I):
            alphas[i] = -Ai / (Bi + Ci * alphas[i - 1])
            betas[i] = (D[i] - Ci * betas[i - 1]) / (Bi + Ci * alphas[i - 1])

        # вычисляем последний слой
        layer[I] = (D[I] - CI * betas[I - 1]) / (BI + CI * alphas[I - 1])
        for i in range(I - 1, -1, -1): # считаем центральную часть слоя (от 1 до I-1)
            # вычисляем слои по рекуррентному прогочному соотношению
            layer[i] = alphas[i] * layer[i + 1] + betas[i]

        # записываем в результирующий массив узел
        # с номером узла, который ближе вешл к нужной пространственной координате
        V[k] = layer[number]
       # print(str(k / K * 100) + "%")

    # построение графика по полученному массиву узлов
    plt.xlabel("t")
    plt.ylabel("V")
    plt.plot(t_array, V, label="Неявная схема, I= " + str(I) + ",K=" + str(K))
    plt.title("Неявная схема")
    plt.legend()
    plt.show()
