import tkinter as tk
from tkinter import messagebox
import Cadastro_Rosto
import Reconhecimento_Menu

def tela_inicial():
    root = tk.Tk()
    root.title("Sistema de Reconhecimento Facial")
    root.geometry("400x300")

    def cadastro():
        root.withdraw()
        Cadastro_Rosto.cadastrar_rosto()
        root.deiconify()

    def reconhecimento():
        root.withdraw()
        Reconhecimento_Menu.reconhecer_rosto()
        root.deiconify()

    label = tk.Label(root, text="Escolha uma opção", font=("Arial", 16))
    label.pack(pady=20)

    botao_cadastro = tk.Button(root, text="Cadastrar Rosto", font=("Arial", 14), command=cadastro)
    botao_cadastro.pack(pady=10)

    botao_reconhecimento = tk.Button(root, text="Reconhecer Rosto", font=("Arial", 14), command=reconhecimento)
    botao_reconhecimento.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    tela_inicial()
