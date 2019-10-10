def meu_in(lista, elemento):
    for e in lista:
        if e == elemento:
            return True

    return False

def intersecao_listas(l1, l2):
    for i in range(len(l1) -1,-1,-1):
        if not meu_in(l2, l1[i]):
            l1.pop(i)

    return l1
