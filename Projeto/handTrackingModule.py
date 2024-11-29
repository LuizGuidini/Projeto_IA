import cv2
import mediapipe as mp

class detectorMaos:
    def __init__(self, confDetec=0.75):
        self.confDetec = confDetec
        self.mpMaos = mp.solutions.hands
        self.maos = self.mpMaos.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=self.confDetec)
        self.mpDraw = mp.solutions.drawing_utils

    def encontrarMaos(self, imagem, desenhar=True):
        imgRGB = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
        self.resultados = self.maos.process(imgRGB)
        if self.resultados.multi_hand_landmarks:
            for maoLandmark in self.resultados.multi_hand_landmarks:
                if desenhar:
                    self.mpDraw.draw_landmarks(imagem, maoLandmark, self.mpMaos.HAND_CONNECTIONS)
        return imagem

    def encontrarPosicao(self, imagem, desenhar=True):
        listaPontos = []
        if self.resultados.multi_hand_landmarks:
            for id, lm in enumerate(self.resultados.multi_hand_landmarks[0].landmark):
                altura, largura, _ = imagem.shape
                cx, cy = int(lm.x * largura), int(lm.y * altura)
                listaPontos.append([id, cx, cy])
                if desenhar:
                    cv2.circle(imagem, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return listaPontos
