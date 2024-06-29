import random
import tkinter as tk

PARTES_FORCA = [
    '''

    ''',
    '''
     |     
     |    
     |    
     |    
    _|_
    ''',
    '''
     _
     |     
     |    
     |    
     |    
    _|_
    ''',
    '''
     _______
     |     
     |    
     |    
     |    
    _|_
    ''',
    '''
     _______
     |     |
     |    
     |    
     |    
    _|_
    ''',
    '''
     _______
     |     |
     |     O
     |    
     |    
    _|_
    ''',
    ''' 
     _______
     |     |
     |     O
     |     |
     |    
    _|_
    ''',
    '''
     _______
     |     |
     |     O
     |    /|
     |    
    _|_
    ''',
    '''
     _______
     |     |
     |     O
     |    /|\\
     |    
    _|_
    ''',
    '''
     _______
     |     |
     |     O
     |    /|\\
     |    / 
    _|_
    ''',
    '''
     _______
     |     |
     |     O
     |    /|\\
     |    / \\
    _|_
    '''
]

def atualizar_forca():
    if T <= 10:
        canvas.delete("all")
        canvas.create_text(400, 150, text=PARTES_FORCA[T], anchor="center", font=("Courier", 18))


def verificar_letra(letra):
    global T, LU, PE, F, FR

    L = letra.lower() 

    if L in LU:
        aviso_letra_usada.config(text='Letra já utilizada!')
        return

    LU.add(L)
    aviso_letra_usada.config(text='')

    acertou = False
    for i in range(FR):
        if F[i].lower() == L:
            PE[i] = F[i]
            acertou = True

    if not acertou:
        T += 1
        atualizar_forca() 
        if T >= 10:
            resultado_jogo.config(text=f'Você perdeu! A palavra era {F}.')
            btn_novo_jogo.place(relx=0.5, rely=0.95, anchor="center") 
            for btn in botoes_letras:
                btn.config(state="disabled")
            return

    if F == ''.join(PE):
        resultado_jogo.config(text=f'Parabéns, você adivinhou!!! A palavra era {F}.')
        btn_novo_jogo.place(relx=0.5, rely=0.95, anchor="center")
        for btn in botoes_letras:
            btn.config(state="disabled")
        return

    label_palavra.config(text=' '.join(PE))

def iniciar_novo_jogo():
    global T, F, FR, PE, LU

    T = 0
    E = random.choice(TUDO)
    if E == Animais:
        F = random.choice(Animais)
        dica = "Tema: Animais"
    elif E == Frutas:
        F = random.choice(Frutas)
        dica = "Tema: Frutas"
    elif E == Biomas:
        F = random.choice(Biomas)
        dica = "Tema: Biomas"

    FR = len(F)
    PE = ['_'] * FR
    LU = set()

    label_palavra.config(text=' '.join(PE))
    label_dica.config(text=dica)
    resultado_jogo.config(text='')
    aviso_letra_usada.config(text='')
    atualizar_forca()

    btn_novo_jogo.place_forget() 
    for btn in botoes_letras:
        btn.config(state="normal")


janela = tk.Tk()
janela.title("Jogo de Adivinhação")

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
janela.geometry(f"{largura_tela}x{altura_tela}+0+0")

canvas = tk.Canvas(janela, width=largura_tela, height=altura_tela)
canvas.pack()

letras = 'abcdefghijklmnopqrstuvwxyz'
botoes_letras = []
for i, letra in enumerate(letras):
    btn_letra = tk.Button(janela, text=letra, width=4, height=2, font=("Helvetica", 18),
                          command=lambda l=letra: verificar_letra(l))
    botoes_letras.append(btn_letra)
    col = i % 13
    row = i // 13
    btn_letra.place(relx=0.1 + col * 0.07, rely=0.75 + row * 0.1)  

btn_novo_jogo = tk.Button(janela, text="Jogar Novamente", width=15, height=2, font=("Helvetica", 18),
                          command=iniciar_novo_jogo)

label_palavra = tk.Label(janela, text="", font=("Courier", 36, "bold"))
label_palavra.place(relx=0.5, rely=0.3, anchor="center")

label_dica = tk.Label(janela, text="", font=("Helvetica", 24))
label_dica.place(relx=0.5, rely=0.4, anchor="center")

aviso_letra_usada = tk.Label(janela, text="", font=("Helvetica", 18), fg="red")
aviso_letra_usada.place(relx=0.5, rely=0.65, anchor="center")  
resultado_jogo = tk.Label(janela, text="", font=("Helvetica", 36, "bold"))
resultado_jogo.place(relx=0.5, rely=0.8, anchor="center")

T = 0
Animais = [
    'gato', 'cachorro', 'elefante', 'girafa', 'leão', 'macaco', 'panda',
    'tigre', 'urso', 'zebra', 'cobra', 'rato', 'galinha', 'porco'
]
Frutas = [
    'maçã', 'banana', 'abacaxi', 'laranja', 'cereja', 'melão', 'abacate',
    'morango', 'kiwi', 'jabuticaba', 'amendoim', 'amêndoa', 'amora',
    'ameixa', 'pitaya'
]
Biomas = [
    'savana', 'deserto', 'montanha', 'floresta', 'praia', 'pantanal',
    'mar', 'oceano', 'pradaria', 'planície', 'planalto', 'caverna',
    'tundra', 'taiga', 'temperado', 'tropical'
]
TUDO = [Animais, Frutas, Biomas]

iniciar_novo_jogo()

janela.mainloop()
