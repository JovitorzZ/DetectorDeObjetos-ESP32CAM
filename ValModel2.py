import cv2
import torch
import numpy as np
import pathlib
from pathlib import Path

# Corrigir Path para rodar no Windows
pathlib.PosixPath = pathlib.WindowsPath

# Caminho do modelo treinado
path = '/best.pt'  # TROQUE PELO CAMINHO DO SEU PESO CASO QUEIRA, ex: yolov5/runs/train/exp9/weights/best.pt

# Carregar o modelo YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'custom', path, force_reload=True)
model.conf = 0.6  # Essa variável determina a acurácia do seu modelo. Faça testes para encontrar o melhor resultado.

print(f"Usando pesos do modelo: {path}")

# Configurar captura de vídeo
# Para webcam, use '0'. Para vídeo, troque o caminho pelo arquivo de vídeo, ex: 'meu_video.mp4'
video_source = 'meu_video.mp4'  # Webcam, ou substitua por 'meu_video.mp4' para usar um vídeo local

cap = cv2.VideoCapture(video_source)

if not cap.isOpened():
    print("Erro ao abrir a fonte de vídeo.")
    exit()

# Loop para captura e processamento de frames
while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar o frame ou fim do vídeo.")
        break

    # Realizar a detecção com YOLOv5
    results = model(frame)

    # Exibir as detecções no frame
    frame = np.squeeze(results.render())  # Renderiza as caixas de detecção
    cv2.imshow('Detecção Local YOLOv5', frame)

    # Pressione 'q' para sair
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Libera a captura e fecha todas as janelas
cap.release()
cv2.destroyAllWindows()
