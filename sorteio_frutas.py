import ttkbootstrap as ttk
import random
from tkinter import messagebox
import sqlite3

#vamos começar criando a janela principal
janela = ttk.Window(themename="cosmo")
janela.title("Sorteio de Frutas")
janela.geometry("900x700")

# ======= FRAME PRINCIPAL =======
# Frame serve para organizar os widgets (rótulos, botões, etc.)
frame_janela = ttk.Frame(janela)
frame_janela.pack(pady=10)  # adiciona o frame à janela com espaçamento vertical

fruta1 = ttk.Label(frame_janela, text="?", font=("Arial",60))
fruta1.pack()

fruta2 = ttk.Label(frame_janela, text="?", font=("Arial",60))
fruta1.pack()

fruta3 = ttk.Label(frame_janela, text="?", font=("Arial",60))
fruta1.pack()


#a gnt vai começar com a lista de frutas
frutas = ["🍇""🍉""🍌""🍍""🍒"]


#agora o sorteio, vamos criar um def sortear para sekecionar as frutas
def sortear():
    fruta1 = random.choice(frutas)
    fruta2 = random.choice(frutas)
    fruta3 = random.choice(frutas)






























janela.mainloop()

