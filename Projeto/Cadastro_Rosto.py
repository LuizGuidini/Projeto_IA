import cv2
import numpy as np
import os

csv_file_path = "rostos_cadastrados.csv"

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def salvar_rosto(id_usuario, rosto_array):
    """Função para salvar o rosto no arquivo CSV"""
    try:
        with open(csv_file_path, 'a') as f:
            rosto_string = " ".join(str(x) for x in rosto_array.flatten())
            f.write(f"{id_usuario},{rosto_string}\n")
            print(f"Rosto do ID {id_usuario} salvo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar o rosto: {e}")

def contar_rostos_cadastrados():
    """Função para contar quantos rostos já estão cadastrados"""
    if not os.path.exists(csv_file_path):
        return 0

    with open(csv_file_path, 'r') as f:
        return len(f.readlines())

def cadastrar_rosto():
    """Função para capturar o rosto e salvar no arquivo"""
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro ao acessar a câmera.")
        return

    numero_rostos = contar_rostos_cadastrados()

    id_usuario = numero_rostos + 1
    print(f"Cadastro de rostos para o ID {id_usuario}.")

    rostos_cadastrados = 0

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

            salvar_rosto(id_usuario, rosto_capturado)

            rostos_cadastrados += 1
            print(f"Rosto {rostos_cadastrados} cadastrado para o ID {id_usuario}.")

            if rostos_cadastrados >= 3:
                print(f"Cadastro de 3 rostos concluído.")
                cap.release()
                cv2.destroyAllWindows()
                return

        cv2.imshow("Cadastro de Rosto", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

