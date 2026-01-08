def este_munte(arr):
    # verifica daca lista formeaza forma de munte
    # caz elementar: daca are mai putin de 3 elemente, nu poate fi munte
    if len(arr) < 3:
        return False

    # gaseste varful: continua pana cand nu mai creste
    varf = 0
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            varf = i + 1
        else:
            break

    # varful nu poate fi la inceput sau sfarsit
    if varf == 0 or varf == len(arr) - 1:
        return False

    # verifica daca scade de la varf pana la sfarsit
    for i in range(varf, len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            return False

    return True


def permutari_munte_recursiv(arr, idx, rezultat):
    # daca am pus toate elementele, verific daca e munte
    if idx == len(arr):
        if este_munte(arr[:]):
            rezultat.append(arr[:])
        return

    # incerc fiecare element pe pozitia curenta
    for i in range(idx, len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]
        permutari_munte_recursiv(arr, idx + 1, rezultat)
        arr[idx], arr[i] = arr[i], arr[idx]  # revin la starea anterioara

def permutari_munte_iterativ(arr):
    # varianta iterativa folosind o stiva
    rezultat = []
    stiva = [(arr[:], 0)] # stiva de tupluri (permutare curenta, index curent)

    while stiva:
        curent, idx = stiva.pop()

        if idx == len(curent):
            if este_munte(curent):
                rezultat.append(curent[:])
            continue

        for i in range(idx, len(curent)):
            nou = curent[:]
            nou[idx], nou[i] = nou[i], nou[idx]
            stiva.append((nou, idx + 1))

    return rezultat
