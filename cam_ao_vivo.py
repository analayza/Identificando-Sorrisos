#coding: utf-8
#_-_Autor: Erlon_-_

import cv2

def detectar_rostos(imagem, classificador):
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Detectar rostos
    rostos_detectados = classificador.detectMultiScale(imagemCinza, scaleFactor=2.5, minNeighbors=8, minSize=(10, 50))

    return rostos_detectados


def mostrar_info_ocorrencias(ocorrencias):
    for (x, y, l, a) in ocorrencias:
        print(f"Ocorrência: x={x}, y={y}, largura={l}, altura={a}")


# Carregar o classificador Haar Cascade para detecção de rostos
padraoRostos = cv2.CascadeClassifier(
    'C:\\Users\\joseb\\PycharmProjects\\ProjetoPDI\\classificadores\\haarcascade_smile.xml')

# Iniciar captura de vídeo da webcam
cap = cv2.VideoCapture(0)

while True:
    # Capturar frame a frame da webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Converter para escala de cinza
    imagemCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos
    faceDetect = detectar_rostos(frame, padraoRostos)

    # Desenhar retângulos ao redor dos rostos detectados
    for (x, y, l, a) in faceDetect:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (255, 0, 0), 5)

    # Exibir o frame com as detecções
    cv2.imshow("Faces encontradas", frame)

    # Mostrar informações sobre as ocorrências
    mostrar_info_ocorrencias(faceDetect)

    # Sair com a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura e fechar todas as janelas
cap.release()
cv2.destroyAllWindows()
