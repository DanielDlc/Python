""" Estrutura formada por listas simulando estrutura de matriz """


def matriz():
    matriz = [[], [], []]
    for num in range(0, 3):
        matriz[0].append(int(input(f"Digite um valor para [0, {num}]: ")))
    for num in range(0, 3):
        matriz[1].append(int(input(f"Digite um valor para [1, {num}]: ")))
    for num in range(0, 3):
        matriz[2].append(int(input(f"Digite um valor para [2, {num}]: ")))
    print("="*31)
    for linha in range(0, 3):
        for coluna in range(0, 3):
            print(f"[{matriz[linha][coluna]:^3}]", end='')
        print()
    print("="*31)


matriz()
