import matplotlib.pyplot as plt
from matplotlib_venn import venn3



conjuntoA= [1, 2, 3, 4, 5, 23, 20]
conjuntoB = [1, 2, 3, 4, 5]






def operarUnion(conjuntoA, conjuntoB):
    conjuntoResultado = []
    for elementoA in conjuntoA:
        if not conjuntoResultado.__contains__(elementoA):
            conjuntoResultado.append(elementoA)

    for elementoB in conjuntoB:
        if not conjuntoResultado.__contains__(elementoA):
            conjuntoResultado.append(elementoB)

    print(conjuntoResultado)


def operarInterseccion(conjuntoA, conjuntoB):
    conjuntoResultado = []

    for elementoA in conjuntoA:
        for elementoB in conjuntoB:
            if elementoA == elementoB:
                conjuntoResultado.append(elementoA)

    print(conjuntoResultado)


def operarDiferencia(conjuntoA, conjuntoB):
    conjuntoResultado = []
    for elementoA in conjuntoA:
        if not conjuntoResultado.__contains__(elementoA):
            conjuntoResultado.append(elementoA)

    for elementoB in conjuntoB:
        if conjuntoResultado.__contains__(elementoB):
            conjuntoResultado.remove(elementoB)

    print(conjuntoResultado)


def operarComplemento(conjuntoA, conjuntoB):
    conjuntoResultado = []
    for elementoB in conjuntoB:
        if not conjuntoResultado.__contains__(elementoB):
            conjuntoResultado.append(elementoB)

    for elementoA in conjuntoA:
        if conjuntoResultado.__contains__(elementoA):
            conjuntoResultado.remove(elementoA)
    print(conjuntoResultado)


def operarCardinalidad(conjunto):
    print(len(conjunto))


def operarSubconjunto(conjuntoA, conjuntoB):
    conjuntoResultado = []

    for elementoB in conjuntoB:
        if conjuntoA.__contains__(elementoB):
            conjuntoResultado.append(elementoB)

    if conjuntoResultado == conjuntoB:
        print("B es subconjunto A")
        return
    print("B NO es subconjunto A")


def operarDisjunto(conjuntoA, conjuntoB):
    conjuntoResultado = []

    for elementoB in conjuntoB:
        if conjuntoA.__contains__(elementoB):
            conjuntoResultado.append(elementoB)

    if conjuntoResultado != conjuntoB:
        print("B es disjunto A")
        return
    print("B NO es disjunto A")

operarUnion(conjuntoA, conjuntoB)
operarInterseccion(conjuntoA, conjuntoB)
operarDiferencia(conjuntoA, conjuntoB)
operarComplemento(conjuntoA, conjuntoB)
operarCardinalidad(conjuntoA)
operarSubconjunto(conjuntoA, conjuntoB)
operarDisjunto(conjuntoA,conjuntoB)


venn3(subsets= (23, 20, 30, 7,8,9,2))



plt.title("Diagrama de Venn de 3 conjuntos")
plt.show()
