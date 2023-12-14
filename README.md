# Instruções

#### Escolha um classificador e deixe nos comentários da atividade qual foi o escolhido.

# Instalando:

```
python -m venv venv

# Windows
. venv/Scripts/activate

# Unix
. venv/bin/activate

pip install -r requirements.txt
```

# Como rodar: 
1. Substitua o classificador ```meu_classificador.xml``` pelo classificador escolhido nos arquivos ```carrega_imagem.py``` e ```cam_ao_vivo.py```


2. Faça com que o ```carrega_imagem.py``` abra no minimo 20 imagens para teste referente ao seu classificador, 15 imagens contendo o objeto que deve ser encontrado e 5 que não possui o objeto, mas possuindo objetos parecidos. Também deve contar o total de ocorrências e as posições onde estão os objetos encontrados (coordenadas x e y, altura e largura)
Execute:
```
python carrega_imagem.py
```

3. Imprima ou use o celular para fazer o teste no arquivo ```cam_ao_vivo.py``` com 10 imagens, 7 com o objeto que deve ser encontrado e 5 com coisas parecidas com o objeto que deve ser encontrado. Também deve contar o total de ocorrências e as posições onde estão os objetos encontrados (coordenadas x e y, altura e largura). Execute:
```
python cam_ao_vivo.py
```

#### O trabalho deverá ser apresentado dia 14, na apresentação, a dupla deve explicar o passo a passo de como funciona o código, o classificador e a operação baseada em convolução que é realizada para a detecção do padrão do classificador. Deve explicar também porque (em caso do classificador achar o objeto mesmo que o objeto não exista) que isso pode acontecer.

#### Também deverá apresentar uma proposta de projeto de aplicação para o mercado envolvendo o classificador escolhido