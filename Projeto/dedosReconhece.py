import cv2
import time
import handTrackingModule as dtm

captura = cv2.VideoCapture(0)
captura.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
captura.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

tac = 0
detector = dtm.detectorMaos(confDetec=0.85)

idPontaDedos = [4, 8, 12, 16, 20]
historicoDedos = []

tempo_inicial = time.time()

while True:
    sucesso, imagem = captura.read()
    imagem = detector.encontrarMaos(imagem)
    listaPntRef = detector.encontrarPosicao(imagem, desenhar=False)

    if len(listaPntRef) != 0:
        Dedos = []
        tolerancia = 20

        # POLEGAR LEVANTADO
        if listaPntRef[idPontaDedos[0]][1] > (listaPntRef[idPontaDedos[0] - 1][1] + tolerancia):
            Dedos.append(1)
        else:
            Dedos.append(0)

        # OUTROS DEDOS
        for id in range(1, 5):
            if listaPntRef[idPontaDedos[id]][2] < (listaPntRef[idPontaDedos[id] - 2][2] - tolerancia):
                Dedos.append(1)
            else:
                Dedos.append(0)

        totalDedos = Dedos.count(1)
        historicoDedos.append(totalDedos)
        if len(historicoDedos) > 10:
            historicoDedos.pop(0)
        totalDedosSuavizado = round(sum(historicoDedos) / len(historicoDedos))

        print(totalDedosSuavizado)

        # retângulo e contagem de dedos
        cv2.rectangle(imagem, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(imagem, str(totalDedosSuavizado), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    tic = time.time()
    fps = 1 / (tic - tac) if (tic - tac) > 0 else 0
    tac = tic
    cv2.putText(imagem, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)  #QUADROS POR SEGUNDO

    cv2.imshow("Image", imagem)

    if time.time() - tempo_inicial > 15:
        if totalDedosSuavizado == 0:
            break

    if cv2.waitKey(1) & 0xFF == 27:
        break

captura.release()
cv2.destroyAllWindows()
