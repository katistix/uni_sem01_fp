from rezolvare import permutari_munte_iterativ, permutari_munte_recursiv
from teste import test_este_munte, test_exemplu, test_permutari_iterativ, test_permutari_recursiv


if __name__ == "__main__":

    # rulam testele
    test_este_munte()
    test_permutari_recursiv()
    test_permutari_iterativ()
    test_exemplu()

    # arr = [7, 10, 14, 16, 18, 27]
    # citim arr din fisierul input
    arr = []
    with open("input.txt") as f:
        items = f.readline().split(" ")
        arr = [int(num) for num in items]

    # rezultat = []
    # permutari_munte_recursiv(arr, 0, rezultat)
    rezultat = permutari_munte_iterativ(arr)


    print(f"lista: {arr}")
    print(f"prmutari munte ({len(rezultat)}):")
    for perm in rezultat:
        print(perm)
