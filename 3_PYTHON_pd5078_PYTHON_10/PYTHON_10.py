

def charakterystyka_bialka(*, sekwencja, masa, pI):
    return f"Białko o sekwencji {sekwencja}, masie {masa} Da oraz punkcie izoelektrycznym {pI}"

def sumuj_cechy_bialek(**cechy):
    masy = [wartosc for klucz, wartosc in cechy.items() if "masa" in klucz]
    suma_mas = sum(masy) if masy else 0

    punkty = [wartosc for klucz, wartosc in cechy.items() if "pI" in klucz]
    srednia_punktow = sum(punkty)/len(punkty) if punkty else None

    if suma_mas != 0 and srednia_punktow:
        return f"Suma mas to {suma_mas}, a średnia punktów izoelektrycznych to {srednia_punktow}."
    elif suma_mas != 0 and srednia_punktow is None:
        return f"Suma mas to {suma_mas}."
    elif suma_mas == 0 and srednia_punktow is not None:
        return f"Średnia punktów izoelektrycznych to {srednia_punktow}"
    else:
        return "Nie podano ani mas, ani punktów izoelektrycznych"

