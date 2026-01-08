from rezolvare import este_munte, permutari_munte_iterativ, permutari_munte_recursiv

# testam functia este_munte
def test_este_munte():
    assert este_munte([10, 16, 27, 18, 14, 7]) == True
    assert este_munte([1, 2, 3]) == False
    assert este_munte([3, 2, 1]) == False
    assert este_munte([1, 3, 2]) == True
    assert este_munte([1, 2]) == False
    assert este_munte([5, 10, 8, 3]) == True

# testam implementarea recursiva
def test_permutari_recursiv():
    arr = [1, 3, 2]
    rezultat = []
    permutari_munte_recursiv(arr, 0, rezultat)
    assert len(rezultat) == 2
    assert [1, 3, 2] in rezultat
    assert [2, 3, 1] in rezultat

# testam implementarea iterativa
def test_permutari_iterativ():
    arr = [1, 3, 2]
    rezultat = permutari_munte_iterativ(arr)
    assert len(rezultat) == 2
    assert [1, 3, 2] in rezultat
    assert [2, 3, 1] in rezultat

# testam exemplul dat in cerinta
def test_exemplu():
    arr = [7, 10, 14, 16, 18, 27]
    rezultat = []
    permutari_munte_recursiv(arr, 0, rezultat)
    assert [10, 16, 27, 18, 14, 7] in rezultat
