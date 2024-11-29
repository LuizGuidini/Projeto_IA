import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox
import time
import subprocess
from Cadastro_Rosto import cadastrar_rosto

csv_file_path = "rostos_cadastrados.csv"

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def reconhecer_rosto():
    cap = cv2.VideoCapture(0)

    rostos_salvos = []
    ids = []

    with open(csv_file_path, 'r') as f:
        for linha in f:
            if linha.strip():
                dados = linha.strip().split(",", 1)
                if len(dados) < 2:
                    print(f"Linha inválida ignorada: {linha.strip()}")
                    continue
                ids.append(dados[0])
                try:
                    rosto_string = dados[1].strip()[1:-1]
                    
                    rosto_string = " ".join(rosto_string.split())
                    rosto_array = np.fromstring(rosto_string, sep=' ', dtype=np.uint8)

                    if rosto_array.size == 150 * 150:
                        rostos_salvos.append(rosto_array.reshape((150, 150)))
                    else:
                        print(f"Array inválido para ID {dados[0]}: Tamanho incorreto.")
                except Exception as e:
                    print(f"Erro ao processar o array do ID {dados[0]}: {e}")
                    continue

    reconhecido = False
    tempo_inicial = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro ao acessar a câmera.")
            break

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rostos = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in rostos:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            rosto_capturado = frame_gray[y:y + h, x:x + w]
            rosto_capturado = cv2.resize(rosto_capturado, (150, 150))

            for i, rosto_salvo in enumerate(rostos_salvos):
                rosto_capturado = cv2.equalizeHist(rosto_capturado) 
                rosto_salvo = cv2.equalizeHist(rosto_salvo)

                diferenca = cv2.norm(rosto_capturado, rosto_salvo, cv2.NORM_L2)
                if diferenca < 4000: #tentar 3000 5000
                    reconhecido = True
                    print(f"Rosto reconhecido! ID: {ids[i]}")
                    cap.release()
                    cv2.destroyAllWindows()

                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("Sucesso", f"Bem-vindo! ID reconhecido: {ids[i]}")
                    root.quit()

                    subprocess.run(["python", "dedosReconhece.py"])
                    
                    abrir_menu_principal()
                    return

        cv2.imshow("Reconhecimento de Rosto", frame)

        if time.time() - tempo_inicial > 20:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if not reconhecido:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Erro", "Nenhum rosto reconhecido. Tente novamente.")
        root.quit()
    
        resposta = messagebox.askquestion("Rosto não cadastrado", "Rosto não encontrado. Deseja voltar para a tela inicial?")
        if resposta == 'yes':
            abrir_tela_inicial()
        else:
            abrir_menu_principal()

def abrir_tela_inicial():
    print("Voltando para a tela inicial...")
    subprocess.run(["python", "Tela_Inicial.py"])

def abrir_menu_principal():
    print("Saindo...")

if __name__ == "__main__":
    reconhecer_rosto()
