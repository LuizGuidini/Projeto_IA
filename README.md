# Projeto_IA 🤖✋
Reconhecimento Facial e Contador de Dedos

Descrição 📑

Este projeto combina tecnologias de Visão Computacional e Reconhecimento Facial com funcionalidades para contagem de dedos, ideal para aplicações que envolvem identificação de usuários e interação simplificada por gestos. Desenvolvido em Python utilizando a biblioteca OpenCV, o sistema realiza:
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
Estrutura do Projeto 📂

O sistema é dividido em quatro módulos principais:

1. Tela_Inicial.py
   
•	Exibe o menu inicial com opções:

o	Cadastrar rosto.

o	Entrar e reconhecer rosto.


2. Cadastro_Rosto.py
   
•	Realiza o registro facial, limitando-se a 3 capturas por sessão.

•	Gera IDs automaticamente para os novos rostos.


3. Reconhecimento_Menu.py
   
•	Reconhece rostos cadastrados.

•	Após 20 segundos sem reconhecimento:

o	Exibe aviso de "Rosto não cadastrado".

o	Oferece opções de cadastro ou retorno ao menu inicial.

•	Chamadas ao módulo Dedos_Reconhece.py em caso de sucesso no reconhecimento.


4. Dedos_Reconhece.py
   
•	Detecta o número de dedos mostrados pela câmera.

•	Mostra a contagem na tela (0 a 5) e o numero de quadros por segundo (FPS).

•	Se não reconhecer nenhum dedo por um tempo ou após reconhecer o numero for "0" fecha o programa.

________________________________________
Tecnologias Utilizadas 🛠️

•	Python

•	OpenCV: Biblioteca de visão computacional.

•	NumPy: Manipulação de arrays e processamento de dados.

________________________________________
Como Executar o Projeto ⬇️

1. Pré-requisitos
   
•	Python 3.8 ou superior.

•	Bibliotecas necessárias:

Copiar código
pip install opencv-python numpy

2. Clonar o Repositório
bash
Copiar código
git clone https://github.com/SeuUsuario/ProjetoReconhecimentoFacial

3. Executar o Sistema
  1.	Navegue até a pasta do projeto:
bash
Copiar código
cd ProjetoReconhecimentoFacial

  2.	Inicie a aplicação:
bash
Copiar código
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

