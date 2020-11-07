""" Função sem parâmetro diferenciando escopo local de global """


def funcao_sem_parametro():  # () parâmetro vazio!
    """ tudo que fica dentro de def é nosso escopo local """
    print('esse é meu escopo local')
    print('esse é meu escopo local')
    print('esse é meu escopo local')


funcao_sem_parametro()  # chamando a mensagem dentro do escopo local três vezes
print()
print('Este é meu escopo Global')
