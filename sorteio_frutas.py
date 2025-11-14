import ttkbootstrap as ttk
import random
from tkinter import messagebox
import sqlite3


 #a gnt vai começar com a lista de frutas
frutas = ["🍇","🍉","🍌","🍍","🍒"]


class Sorteio:
    def __init__(self):
        #vamos começar criando a janela principal
        self.janela = ttk.Window(themename="cosmo")
        self.janela.title("Sorteio de Frutas")
        self.janela.geometry("900x700")


        titulo = ttk.Label(self.janela, text="Sorteio de Frutas 🎰", font=("Helvetica", 24, "bold"))
        titulo.pack(pady=15)

        # ======= FRAME PRINCIPAL =======
        # Frame serve para organizar os widgets (rótulos, botões, etc.)
        frame_janela = ttk.Frame(self.janela)
        frame_janela.pack(pady=10)  # adiciona o frame à janela com espaçamento vertical

        self.fruta1 = ttk.Label(frame_janela, text="?", font=("Arial",60))
        self.fruta1.pack(side='left', padx=10)

        self.fruta2 = ttk.Label(frame_janela, text="?", font=("Arial",60))
        self.fruta2.pack(side='left', padx=10)

        self.fruta3 = ttk.Label(frame_janela, text="?", font=("Arial",60))
        self.fruta3.pack(side='left', padx=10)

        #botao de sortear
        self.button_sortear = ttk.Button(self.janela, text="Sortear!", bootstyle="success-outline", command=self.sortear)
        self.button_sortear.pack(pady=20, ipadx=20, ipady=10)

        ttk.Label(self.janela, text="Histórico de Jogadas", font=("Helvetica", 16)).pack(pady=(10, 5))

          # Frame que conterá o Treeview e a scrollbar para organizá-los.
        tree_frame = ttk.Frame(self.janela)
        tree_frame.pack(fill="both", expand=True, padx=20, pady=10)



    def sortear(self):
        fruta1 = random.choice(frutas)
        fruta2 = random.choice(frutas)
        fruta3 = random.choice(frutas)

        #atualizar a tela
        self.fruta1.config(text=)








       


        #agora o sorteio, vamos criar um def sortear para sekecionar as frutas






    # Método que inicia o loop principal da interface gráfica.
    def run(self):
        self.janela.mainloop()



if __name__ == "__main__":

    # Instanciar a classe da aplicação — cria a janela e prepara tudo.
    app = Sorteio()

    # Rodar o loop principal — mantém a interface gráfica responsiva até o usuário fechar.
    app.run()

