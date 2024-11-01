# Detector de Objetos - NEXT 2024: YOLOv5 e ESP32-CAM

## Introdução
O projeto foi desenvolvido para solucionar a necessidade de identificar pessoas em situações de risco durante enchentes, como as que ocorreram em abril de 2024 no estado do Rio Grande do Sul. Esse tipo de desastre natural frequentemente resulta em dificuldades para localizar pessoas em áreas inundadas, dificultando operações de resgate e aumentando os riscos para as equipes envolvidas.

Utilizando o modelo de detecção de objetos **YOLOv5** e o módulo **ESP32-CAM**, o sistema é capaz de identificar e localizar pessoas em tempo real em cenários de enchente, proporcionando suporte crucial para equipes de resgate.

---

## Criação de Novas Imagens e Organização dos Dados
Inicialmente, meu dataset foi composto de 79 fotos do cenário. Para melhorar o treino do meu modelo, utilizei o [Roboflow](https://roboflow.com/) para auxiliar na criação de novas imagens com as seguintes argumentações:

- **Crop:** 0% Minimum Zoom, 30% Maximum Zoom
- **Grayscale:** Aplicar em 25% das imagens
- **Saturation:** Entre -34% e +34%
- **Brightness:** Entre -25% e +25%
- **Exposure:** Entre -15% e +15%
- **Blur:** Até 4.9px
- **Noise:** Até 1.96% dos pixels

Após a geração de novas imagens e a criação das labels do meu dataset agora está composto por 237 Imagens, onde optei por dividir o conjunto de dados em uma proporção de **80/20** para o treinamento e validação do modelo.

![Organização dos dados](assets/data.png)

### Segue o link do dataset: [DATA](DATA)

### Descrição dos Componentes:

- **Pasta `/images/train`**: Armazena as imagens destinadas ao treinamento do modelo, representando 70% do conjunto de dados. Essas imagens são usadas para ajustar os pesos do modelo durante o processo de aprendizado.

- **Pasta `/images/val`**: Armazena as imagens usadas para validação do modelo, representando 30% do conjunto de dados. O modelo é testado nessas imagens durante o treinamento para verificar o desempenho em dados que ele ainda não viu.

- **Pasta `/labels/train`**: Armazena os arquivos de **labels** correspondentes às imagens de treino. Cada arquivo de label segue o formato do YOLO (classe, x_center, y_center, width, height), indicando a classe e a posição dos objetos nas imagens.

- **Pasta `/labels/val`**: Armazena os arquivos de **labels** correspondentes às imagens de validação. Eles são usados para avaliar a precisão das detecções do modelo nas imagens do conjunto de validação.

Essa estrutura de diretórios facilita a gestão dos dados durante o treinamento e validação do modelo, assegurando que tanto as imagens quanto as labels estejam organizadas de forma otimizada para o processo de aprendizagem.

---

## Treinamento do Modelo
Para treinar o modelo, utilizei o [Google Colab](https://colab.google/). 

Para iniciar o treinamento:
1. Instancie um T4 GPU, clicando em "Alterar Tipo de Ambiente de Execução" para ativar a GPU do Colab.
2. Faça o upload do arquivo [Treinamento.pynb](Treinamento.ipynb).
3. Salve o arquivo `best.pt` que é gerado como resultado do treinamento.
   
**Caminho do `best.pt`:**

![image](https://github.com/user-attachments/assets/5f12ae25-3a39-4b82-a85e-d8817666cdb0)

---

## Gravando o seu ESP32 CAM
Agora com seu `best.pt` entre no arquivo: [ReconhecedorDeObjetos.ino](ReconhecedorDeObjetos.ino) e faça as alterações em:

```cpp
//ATENÇÃO!
//Caso esteja roteando do seu celular da Apple não irá funcionar, porque ele não tem 2.4GHz até o momento em que este projeto foi realizado.
const char* WIFI_SSID = "ssid wifi celular"; // Colocar nome da rede WI-FI
const char* WIFI_PASS = "senha"; // Colocar Senha do WI-FI
```
---

## Validação do modelo 

* Para validar seu modelo utilizando o ESP-32 CAM utilize o arquivo [ValModel.py](ValModel.py)

  Vídeo do modelo funcionando com o ESP-32 CAM no NEXT 2024: https://youtu.be/BiFk6Dx35h8

* Caso opte por validar via vídeo utilize o aqruivo [ValModel2.py](ValModel2.py)

  Vídeo do modelo funcionando sendo validado via arquivo.mp4: https://youtu.be/JJD3XtoOA8M

Após executar o seu código no VsCode, uma janela pop-up do Python será aberta, mostrando as imagens capturadas pela câmera do ESP32-CAM ou o Vídeo caso tenha optado por utilizar o ValModel2.


