def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio            # achou
        elif lista[meio] < alvo:
            inicio = meio + 1      # procura na metade direita
        else:
            fim = meio - 1         # procura na metade esquerda

    return -1                      # não achou


numeros = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]  # precisa estar ordenada

print(busca_binaria(numeros, 23))  # 5
print(busca_binaria(numeros, 7))   # -1