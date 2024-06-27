import random

while True:
    TE = 10
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
        print(f'O tema será Animais')
    elif E == Frutas:
        F = random.choice(Frutas)
        print(f'O tema será Frutas')
    elif E == Biomas:
        F = random.choice(Biomas)
        print(f'O tema será Biomas')
    print()
    FR = len(F)
    PE = ['_'] * FR
    LU = set()
    while T < 10:
        print(' '.join(PE))
        L = input('Digite 1 letra: ').lower()
        while len(L) != 1 or not L.isalpha() or L in LU:
            L = input(
                'Por favor, digite apenas 1 letra que ainda não foi usada: ')
        LU.add(L)
        print(LU)
        if L == '!':
            print(f'A dica é {F}')
            continue
        acertou = False
        for i in range(FR):
            if F[i].lower() == L:
                PE[i] = F[i]
                acertou = True
        if not acertou:
            T += 1
            if T == 1:
                TE -= 1
                print('''
|_______
|    0
|   
|  
|    
|   
|   
|_________
''')
                print('\n'
                      f'você ainda tem {TE} tentativas'
                      '\n')
            elif T == 2:
                print('''
    |_______
    |    0
    |    |
    |  
    |   
    |   
    |   
    |_________
    ''')
                TE -= 1
                print('\n'
                      f'você ainda tem {TE} tentativas'
                      '\n')
            elif T == 3:
                print('''
    |_______
    |    0
    |    |
    |    |
    |    
    |   
    |   
    |_________
    ''')
                TE -= 1
                print('\n'
                      f'você ainda tem {TE} tentativas'
                      '\n')
            elif T == 4:
                print('''
    |_______
    |    0
    |    |
    |    | 
    |    |
    |   
    |  
    |_________
    ''')
                TE -= 1
                print('\n'
                      f'você ainda tem {TE} tentativas'
                      '\n')
            elif T == 5:
                print('''
    |_______
    |    0
    |   ||
    |  | |
    |    |
    |   
    |  
    |_________
    ''')
                TE -= 1
                print('\n'
                      f'você ainda tem {TE} tentativas'
                      '\n')
            elif T == 6:
                print('''
    |_______
    |    0
    |   ||| 
    |  | | |
    |    |
    |   
    |   
    |_________
    ''')
                TE -= 1
                print('\n'
                      f'você ainda tem {TE} tentativas'
                      '\n')
            elif T == 7:
                print('''
    |_______
    |    0
    |   ||| 
    |  | | |
    |    |
    |   | 
    |   
    |_________
    ''')
                TE -= 1
                print('\n'
                      f'você ainda tem {TE} tentativas'
                      '\n')
            elif T == 8:
                print('''
    |_______
    |    0
    |   ||| 
    |  | | |
    |    |
    |   | 
    |   | 
    |_________
    ''')
                TE -= 1
                print('\n'
                      f'você ainda tem {TE} tentativas'
                      '\n')
            elif T == 9:
                print('''
    |_______
    |    0
    |   ||| 
    |  | | |
    |    |
    |   | |
    |   | 
    |_________
    ''')
                TE -= 1
                print('\n'
                      f'você ainda tem {TE} tentativa restante'
                      '\n')
            elif T == 10:
                print('''
    |_______
    |    0
    |   ||| 
    |  | | |
    |    |
    |   | |
    |   | |
    |_________
    ''')
            if T >= 10:
                print(f'Você perdeu! A palavra era {F}')
                break
        if F == ''.join(PE):
            print(f'Parabéns, você adivinhou!!! A palavra era {F}')
            break
    print()
    print('Deseja jogar novamente?')
    print('1 - Sim')
    print('2 - Não')
    J = input('Digite sua escolha: ')
    print()
    if J != '1':
        break

