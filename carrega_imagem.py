#coding: utf-8
#_-_Autor: Erlon_-_

import cv2
import os

def detectar_rostos(imagem, classificador):
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Detectar rostos
    #rostos_detectados = classificador.detectMultiScale(imagemCinza, scaleFactor=2.5, minNeighbors=8, minSize=(70, 70))
    rostos_detectados = classificador.detectMultiScale(imagemCinza, scaleFactor=4.2, minNeighbors=15, minSize=(30, 70))


    return rostos_detectados

def mostrar_info_ocorrencias(total_ocorrencias, ocorrencias):
    print(f"Total de Ocorrências: {total_ocorrencias}")
    for i, (x, y, l, a) in enumerate(ocorrencias, start=1):
        print(f"Ocorrência {i}: x={x}, y={y}, largura={l}, altura={a}")

def rodar_imagens(caminho_da_pasta, classificador):
    total_ocorrencias = 0

    for nome_do_arquivo in os.listdir(caminho_da_pasta):
        if nome_do_arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            caminho_completo = os.path.join(caminho_da_pasta, nome_do_arquivo)
            imagem = cv2.imread(caminho_completo)

            ocorrencias = detectar_rostos(imagem, classificador)
            total_ocorrencias += len(ocorrencias)

            mostrar_info_ocorrencias(len(ocorrencias), ocorrencias)

            # Desenhar retângulos ao redor dos rostos detectados
            for (x, y, l, a) in ocorrencias:
                cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 0), 5)

            # Exibir o frame com as detecções
            cv2.imshow("Faces encontradas", imagem)
            cv2.waitKey()

    # Mostrar informações no final
    print(f"Total de Ocorrências em todas as imagens: {total_ocorrencias}")

# Carregar o classificador Haar Cascade para detecção de rostos
padraoRostos = cv2.CascadeClassifier('C:\\Users\\joseb\\PycharmProjects\\ProjetoPDI\\classificadores\\haarcascade_smile.xml')

# Rodar imagens da pasta
caminho_da_pasta = 'C:\\Users\\joseb\\PycharmProjects\\ProjetoPDI\\Imagens'
rodar_imagens(caminho_da_pasta, padraoRostos)

# fechar todas as janelas
cv2.destroyAllWindows()