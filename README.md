# Projeto_IA 🤖✋
Reconhecimento Facial e Contador de Dedos

Descrição 📑

Este projeto combina tecnologias de Visão Computacional e Reconhecimento Facial com funcionalidades para contagem de dedos, ideal para aplicações que envolvem identificação de usuários e interação simplificada por gestos. Desenvolvido em Python utilizando a biblioteca OpenCV, frameworks como o MediaPipe e o algoritmos de detecção de rostos haarcascade_frontalface, o sistema realiza:

1.	Cadastro e reconhecimento facial.
2.	Contador de dedos reconhecidos, mostrando numeros e FPS na tela.
3.	Tratamento de exceções e fluxos claros para usuários não reconhecidos.
   
________________________________________
Funcionalidades 🔍

•	Cadastro Facial: Registra rostos para futuras identificações.

•	Reconhecimento Facial: Identifica rostos previamente cadastrados.

•	Contagem de Dedos: Após o reconhecimento, detecta e conta dedos e se não reconhecer nenhum dedo por um tempo ou após reconhecer o numero for "0" fecha o programa.

•	Fluxo Alternativo: Para rostos não reconhecidos, exibe opções para cadastrar ou retornar à tela inicial.

________________________________________
Arquivos e Estrutura do Projeto 📂


1. Tela_Inicial.py

   •	Exibe o menu principal com as opções:

         o	Cadastrar Rosto.

         o	Entrar e Reconhecer (inicia o reconhecimento facial).


2. Cadastro_Rosto.py
   
   •	Captura e salva três imagens do rosto na pasta rostos_cadastrados.

   •	IDs gerados automaticamente para facilitar a identificação.


3. Reconhecimento_Menu.py
   
   •	Utiliza o cv2.norm para medir a diferença entre o rosto capturado e os rostos cadastrados.

   •	Limite de 10 segundos para identificar um rosto. Após isso:

         o	Exibe aviso de "Rosto não cadastrado".

         o	Oferece opções de cadastro ou retorno ao menu inicial.

   •	Chama o módulo Dedos_Reconhece.py em caso de sucesso no reconhecimento.


4. Dedos_Reconhece.py
   
   •	Utilizamos o framework MediaPipe, desenvolvido pela google de codigo aberto, para detectar imagens e videos.

   •	Usa algoritmos de rastreamento de mão (HandTrackingModule) para identificar dedos levantados.

   •	Mapeia o número de dedos levantados(0 a 5) e o numero de quadros por segundo (FPS).

   •	Se não reconhecer nenhum dedo por um tempo ou após reconhecer o numero for "0" fecha o programa.


6. Recursos Adicionais
   
   •	haarcascade_frontalface_default.xml: Algoritmo pré-treinado da OpenCV para detecção de rostos.

   •	HandTrackingModule: Módulo externo para rastreamento de mãos e contagem de dedos.

   •	Pasta rostos_cadastrados/: Armazena imagens dos rostos registrados para comparação futura.


________________________________________
Como Funciona o Cadastro e Reconhecimento de Rostos? 🧠

Cadastro

1.	Captura três imagens do rosto com a câmera.
   
2.	Salva as imagens na pasta rostos_cadastrados com IDs automáticos.

   
Reconhecimento

1.	Utiliza o cv2.norm para comparar o vetor do rosto capturado com os vetores dos rostos salvos:
   
         o	cv2.norm calcula a distância euclidiana entre os vetores, representando a diferença entre imagens.

2.	O limite de similaridade (4000, ajustável) define se o rosto será considerado reconhecido ou não.


________________________________________
Como Funciona a Contagem de Dedos? ✋

1.	O HandTrackingModule detecta a posição das mãos usando marcadores específicos nos dedos.

2.	Os dedos levantados são contados com base no ângulo entre os pontos:

         o	Se o dedo estiver reto (ângulo acima do limiar), ele é contado como "levantado".

3.	A contagem é mapeada mostrando no video (0 a 5).


________________________________________
Tecnologias Utilizadas 🛠️

•	Python

•	OpenCV: Detecção facial e rastreamento de características visuais.

•	NumPy: Processamento de matrizes e vetores.

•	HandTrackingModule: Rastreamento de mãos para contagem de dedos.


________________________________________
Como Executar o Projeto ⬇️

1. Pré-requisitos
   
•	Python 3.8 ou superior.

•	Bibliotecas necessárias:

         pip install opencv-python numpy

2. Clonar o Repositório

         git clone https://github.com/SeuUsuario/ProjetoReconhecimentoFacial

3. Executar o Sistema
   
     1.	Navegue até a pasta do projeto:

            cd ProjetoReconhecimentoFacial

     2.	Inicie a aplicação:

            python Tela_Inicial.py


________________________________________
Fluxo de Operação 🚀

1.	Tela Inicial: Escolha entre cadastrar rosto ou reconhecer usuário.

2.	Cadastro: Capture o rosto 3 vezes para registrá-lo.

3.	Reconhecimento: Se reconhecido, acesse o menu de contagem de dedos.

4.	Erro no Reconhecimento: Após 20 segundos, escolha cadastrar ou voltar.


________________________________________
Contribuição 🤝

Para contribuir com melhorias ou correções, sinta-se à vontade para abrir Issues ou enviar um Pull Request no repositório.

________________________________________
Autores 🥇

•	Márcia Guidini

•	Luiz Guidini

