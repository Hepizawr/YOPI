import math
import matplotlib.pyplot as plt
import numpy as np

Film = []


def FileReadToMas(File_name, Mas):
    r = open(File_name)
    for item in r:
        Mas.append(int(item))
    r.close()


def FileReadToConsole(File_name):
    r = open(File_name)
    for item in r:
        print(item, end='')
    r.close()


def MidValOfMas(Mas):
    x_mid = 0
    for i in Mas:
        x_mid += i
    x_mid = x_mid / len(Mas)
    return x_mid


def MediOfMas(Mas):
    if len(Mas) % 2 == 0:
        medi = (Mas[int(len(Mas) / 2)] + Mas[int(len(Mas) / 2) - 1]) / 2
    else:
        mid_mas = int(len(Mas) / 2)
        medi = Mas[mid_mas]
    return medi


def ModaOfMas(Mas):
    a_set = sorted(set(Mas))

    qty_most_common = 0
    moda = []

    for item in a_set:
        qty = Mas.count(item)
        if qty > qty_most_common:
            qty_most_common = qty

    if qty_most_common == 1:
        return "Моди не має"
    else:
        for item in a_set:
            if Mas.count(item) == qty_most_common:
                moda.append(item)
    return moda


def DisperOfMas(Mas):
    upper = 0
    for i in Mas:
        upper += (i - MidValOfMas(Mas)) ** 2

    disper = (upper / (len(Mas)))
    return disper


def MidSqrDevOfMas(Mas):
    return math.sqrt(DisperOfMas(Mas))


def TablOfFreq(Mas, mode):
    a_set = set(Mas)

    if mode == 'C':
        mode = None

    print("Значеня:\t\t\t", end="", file=mode)
    for item in sorted(a_set):
        print(item, end="\t", file=mode)

    print("\nКількість:\t\t\t", end="", file=mode)
    for item in sorted(a_set):
        print(Mas.count(item), end="\t", file=mode)

    print("\nCукупна частота:\t", end="", file=mode)
    sum = 0
    for item in sorted(a_set):
        sum += Mas.count(item)
        print(sum, end="\t", file=mode)


def HistOfMas(Mas):
    Sort_Mas = sorted(Mas)
    Mas_min = Sort_Mas[0]
    Mas_max = Sort_Mas[-1]
    Znac = []

    # if len(Mas) % 2 == 0:
    #     n = np.sqrt(len(Mas))
    # else:
    #     n = np.sqrt(len(Mas)) - 1
    #
    # h = ((Mas_max - Mas_min) / n)
    #
    # i = Mas_min
    #
    # while i < Mas_max:
    #     i += h
    #     Znac.append(i)
    #
    # Znac.insert(0, 1)
    # Znac[-1] = Mas_max
    #
    # print(Znac)

    n = 1 + (3.322 * np.log10(len(Sort_Mas)))
    h = round((Mas_max - Mas_min) / n)

    i = Mas_min
    while i < Mas_max:
        i += h
        Znac.append(i)

    Znac.insert(0, Mas_min)
    Znac[-1] = Mas_max
    print(Znac)

    plt.hist(Sort_Mas, bins=Znac)
    plt.show()


def WriteToFile(Mas):
    w = open("Resault.txt", "w")

    w.write("Масив значень: ")
    w.write("\n" + str(Mas))
    w.write("\n\nСередне значення: ")
    w.write("\n" + str(MidValOfMas(Mas)))
    w.write("\n\nМедіана вибірки: ")
    w.write("\n" + str(MediOfMas(Mas)))
    w.write("\n\nМода вибірки: ")
    w.write("\n" + str(ModaOfMas(Mas)))
    w.write("\n\nДисперсія: ")
    w.write("\n" + str(round(DisperOfMas(Mas), 4)))
    w.write("\n\nСереднє квадратичне відхилення розподілу: ")
    w.write("\n" + str(round(MidSqrDevOfMas(Mas), 4)))
    w.write("\n\nТаблиця частот: \n")
    TablOfFreq(Mas, w)


FileReadToMas("10_films.txt", Film)

WriteToFile(Film)

FileReadToConsole("Resault.txt")

HistOfMas(Film)


# print("Масив значень: ")
# print(Film)
#
# print("\nСередне значення: ")
# print(MidValOfMas(Film))
#
# print("\nМедіана вибірки: ")
# print(MediOfMas(Film))
#
# print("\nМода вибірки: ")
# print(ModaOfMas(Film))
#
# print("\nДисперсія: ")
# print(round(DisperOfMas(Film), 4))
#
# print("Середнє квадратичне відхилення розподілу: ")
# print(round(MidSqrDevOfMas(Film), 4))
#
# print("\nТаблиця частот: ")
# print(TablOfFreq(Film, 'C'))
