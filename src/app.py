from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from src.model import Grafo

grafo = Grafo()

estados_partida = [
    '', 'AC', 'AL', 'AM', 'AP', 'BA', 'CE',
    'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT',
    'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN',
    'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'
]

cores = {
    'preto': '#242323',
    'cinza': '#c1c4be',
    'cinza_claro': '#e6e1e5',
    'branco': '#ffffff',
    'azul': '#2176C1'
}


def selecionar(e):
    """
    Capta o evento associado a seleção de um estado
    na Combobox do estado de partida.
    """

    # Limpa o campo do estado de chegada caso
    # tenha o mesmo estado no campo do estado
    # de partida.
    if combo_estado_partida.get() == combo_estado_chegada.get():
        combo_estado_chegada.set('')

    # Limpa e reseta o campo do estado de chegada
    # caso selecione a opção vazia no campo
    # do estado de partida.
    if combo_estado_partida.get() == '':
        combo_estado_chegada.set('')
        combo_estado_chegada.config(value=[''])

    # Ajusta a lista de opções de estados de chegada
    # para não conter o estado que foi selecionado
    # como o de partida.
    else:
        estado = combo_estado_partida.get()
        estados_chegada = estados_partida.copy()
        estados_chegada.pop(estados_chegada.index(estado))
        estados_chegada.pop(estados_chegada.index(''))
        combo_estado_chegada.config(value=estados_chegada)


def calcular_trajeto():
    estado_partida = combo_estado_partida.get()
    estado_chegada = combo_estado_chegada.get()

    if estado_partida == '' or estado_chegada == '':
        return

    if grafo.existe_aresta(estado_partida, estado_chegada):
        print(f"Os estados {grafo.estados[estado_partida]} e {grafo.estados[estado_chegada]} fazem fronteira.")
    else:
        print("Não tem fronteira entre esses estados")


# Instância da janela
app = Tk()
app.title('Mapa Brasil')
app.geometry('800x600')
app.maxsize(1000, 650)
app.config(bg=cores['cinza'])

titulo = Label(app, text="Bem-vindo", bg=cores['azul'], fg=cores['branco'], relief=RAISED)
titulo.pack(ipady=5, fill='x')
titulo.config(font=("Font", 30))


frame_selecao = Frame(app, bg=cores['cinza_claro'])
frame_selecao.pack(pady=5)


frame_partida = Frame(frame_selecao, bg=cores['branco'])
frame_partida.grid(row=0, column=0, padx=10, pady=10)

Label(frame_partida, text="Escolha o estado de partida", bg=cores['branco']).pack(side="top", pady=5)
combo_estado_partida = ttk.Combobox(frame_partida, value=estados_partida, width=30)
combo_estado_partida.pack(side="bottom", padx=5, pady=5)
combo_estado_partida.current(0)
combo_estado_partida.bind("<<ComboboxSelected>>", selecionar)


frame_chegada = Frame(frame_selecao, bg=cores['branco'])
frame_chegada.grid(row=0, column=1, padx=10, pady=10)

Label(frame_chegada, text="Escolha o estado de chegada", bg=cores['branco']).pack(side="top", pady=5)
combo_estado_chegada = ttk.Combobox(frame_chegada, value=[''], width=30)
combo_estado_chegada.current(0)
combo_estado_chegada.pack(side="bottom", padx=5, pady=5)


frame_botao = Frame(frame_selecao)
botao_calcular = Button(frame_selecao, text="Calcular trajeto", command=calcular_trajeto)
botao_calcular.grid(row=0, column=2, padx=10, pady=10)


brasilFrame = Frame(app, bg=cores['preto'])
brasilFrame.pack(pady=15)

mapa_path = '../assets/mapaBR.jpg'
img_mapa = ImageTk.PhotoImage(Image.open(mapa_path))
Label(brasilFrame, image=img_mapa).grid(row=0, column=0, padx=5, pady=5)


app.mainloop()
