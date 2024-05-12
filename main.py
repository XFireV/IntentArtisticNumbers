import random

while True:
    T = 0
    Animais = [
        'gato', 'cachorro', 'elefante', 'girafa', 'leão', 'macaco', 'panda',
        'tigre', 'urso', 'zebra', 'cobra', 'rato', 'galinha', 'porco'
    ]
    Frutas = [
        'maca', 'banana', 'abacaxi', 'laranja', 'cereja', 'melao', 'abacate',
        'morango', 'kiwi', 'jabuticaba', 'amendoim', 'amendôa', 'amora',
        'ameixa', 'pitaia'
    ]
    Biomas = [
        'savana', 'deserto', 'montanha', 'floresta', 'praia', 'pantanal',
        'mar', 'oceano', 'pradaria', 'planície', 'planalto', 'caverna',
        'tundra', 'taiga', 'temperado', 'tropical'
    ]
    TUDO = [Animais, Frutas, Biomas]
    E = random.choice(TUDO)
    if E == Animais:
        F = random.choice(Animais)
        print(f'o tema será Animais')
    elif E == Frutas:
        F = random.choice(Frutas)
        print(f'o tema será Frutas')
    elif E == Biomas:
        F = random.choice(Biomas)
        print(f'o tema será Biomas')
    print()
    FR = len(F)
    PE = ['_'] * FR
    for i in range(20):
        print(' '.join(PE))
        L = input('digite 1 letra: ')
        while len(L) > 1:
            L = input('Por favor, digite apenas 1 letra')
        acertou = False
        for i in range(FR):
            if F[i].lower() == L.lower():
                PE[i] = F[i]
                acertou = True
        if not acertou:
            T += 1
        if T > 10:
            print('Você perdeu')
            break
        if T == 1:
            print('''
                    ___''')
        elif T == 2:
            print(''' 
                      |
                      |
                      |
                      |___|''')
        if F == ''.join(PE):
            print(f'Parabéns, você adivinhou!!! a palavra era {F}')
            break
    print()
    print('Deseja jogar novamente?')
    print('1 - Sim')
    print('2 - Não')
    J = input('Digite sua escolha: ')
    print()
    if J != '1':
        break
