""" fila de pessoas """


def fila():
    fila = ['Daniel', 'Alessandro', 'Miguel']
    fila.append('Bia')  # append adiciona elemento acima da fila
    fila.append('Zen')
    fila.append('Lion')
    fila.append('Luke')
    fila.append('Pequeno')

    print(f'Atualmente existem essas pessas: {fila} na fila')
    print()
    fila.pop(0)  # pop zero remove o primeiro nome da fila
    print(fila)
    fila.pop(0)
    print(fila)
    fila.pop(0)
    print(fila)
    print('foram removidos os primeiros 3 nomes da fila')


fila()
