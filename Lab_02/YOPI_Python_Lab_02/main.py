import matplotlib.pyplot as plt
import math

Arr = []
Arr_test = [8, 9, 12, 13, 16, 17, 18, 20, 22, 30, 31, 40]
Arr_test2 = [60, 55, 74, 68, 78, 45, 83, 40, 60, 85, 50, 70]


# Arr = [1, 2, 4, 7, 8, 9, 10, 12]

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


def quantile(Mas, Piece):
    Mas_sort = sorted(Mas)

    A = Piece * (len(Mas_sort) + 1)

    A_int = int(A)

    A_dif = A - A_int

    Q = Mas_sort[A_int - 1] + A_dif * (Mas_sort[A_int] - Mas_sort[A_int - 1])
    return Q


def MidValOfMas(Mas):
    x_mid = 0
    for i in Mas:
        x_mid += i
    x_mid = x_mid / len(Mas)
    return x_mid


def DisperOfMas(Mas):
    upper = 0
    for i in Mas:
        upper += (i - MidValOfMas(Mas)) ** 2
    disper = (upper / (len(Mas) - 1))
    return disper


def MidSqrDevOfMas(Mas):
    return math.sqrt(DisperOfMas(Mas))


def MAD(Mas):
    upper = 0
    for i in Mas:
        upper += abs(i - MidValOfMas(Mas))
    mad = (upper / (len(Mas)))
    return mad


def LinerTransform(Mas, mid, stnd, mode):
    if mode == 'C':
        mode = None

    mid_x = MidValOfMas(Mas)
    Arr_tranform = []

    a = (stnd - mid) / (100 - mid_x)
    b = ((100 * mid) - (stnd * mid_x)) / (100 - mid_x)

    for item in Mas:
        y = (a * item) + b
        Arr_tranform.append(round(y, 2))

    print(str(f"y={round(a, 4)}x+{round(b, 4)}"), file=mode)
    print(str(Mas), file=mode)
    print("Cереднє значення " + str(round(MidValOfMas(Mas), 4)), file=mode)
    print(str(Arr_tranform), file=mode)
    print("Cереднє значення " + str(round(MidValOfMas(Arr_tranform))), file=mode)


    return Arr_tranform


def SteamLeaf(Mas, mode):
    if mode == 'C':
        mode = None

    Mas_sort = sorted(Mas)

    Mas11 = []
    Mas10 = []
    Mas01 = []

    for item in Mas_sort:
        Mas11.append(item / 10)

    # print(Mas01)

    for item in Mas11:
        Mas10.append(int(item))

    Mas_set = set(Mas10)

    i = 0
    while i < len(Mas10):
        Mas01.append(int(10 * round(Mas11[i] - Mas10[i], 1)))
        i += 1

    i = 0
    for item_set in Mas_set:
        print(f"{item_set}| ", end="", file=mode)
        while Mas10[i] == item_set:
            print(Mas01[i], end=" ", file=mode)
            i += 1
            if i == len(Mas10): break
        print("", file=mode)

    print("Key: 2|3 means 23", file=mode)


def BarOfMas(Mas):
    Mas_set = set(Mas)
    Mas_values = []
    Mas_set_values = []

    for item in Mas_set:
        Mas_set_values.append(item)

    for item in Mas_set:
        Mas_values.append(Mas.count(item))

    print(Mas_set_values, end="\n")
    print(Mas_values)
    plt.bar(Mas_set_values, Mas_values)
    plt.show()


def BoxplotOfMas(Mas):
    plt.boxplot(Mas)
    plt.show()


def WriteToFile(Mas):
    w = open("Resault.txt", "w")

    w.write("Квантилі і персантиль: ")
    w.write("\nQ1 " + str(quantile(Mas, 0.25)))
    w.write("\nQ3 " + str(quantile(Mas, 0.75)))
    w.write("\nP90 " + str(quantile(Mas, 0.9)))
    w.write("\n\nCереднє та стандартне відхилення: ")
    w.write("\n" + str(round(MidSqrDevOfMas(Mas), 4)))
    w.write("\n" + str(round(MAD(Mas), 4)))
    w.write("\n\nЛінійне перетворення: \n")
    # w.write("\n" + str(Mas))
    # w.write("\nCереднє значення " + str(MidValOfMas(Mas)))
    # w.write("\n" + str(LinerTransform(Mas, 95, 100)))
    # w.write("\nCереднє значення " + str(round(MidValOfMas(LinerTransform(Mas, 95, 100)), 0)))
    LinerTransform(Mas, 95, 100, w)
    w.write("\n\nДіаграма 'стовбур – листя': \n")
    SteamLeaf(Mas, w)


FileReadToMas("input_10.txt", Arr)

# WriteToFile(Arr)
#
# FileReadToConsole("Resault.txt")
#
# BoxplotOfMas(Arr)

print(sorted(Arr))
print(MidValOfMas(Arr))
print(DisperOfMas(Arr))
print(MidSqrDevOfMas(Arr))
print(MAD(Arr))
