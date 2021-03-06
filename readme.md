# API Agenda
___

### Descrição da API:
Trata-se de uma API Rest que utiliza apenas JSON e guarda contratos.
Cada contato possui:
1. id(Int)
2. nome(String)
3. canal(ENUM - 'email', 'celular' ou 'fixo')
4. valor(String. Ex: 22-99421 4839, marcos@gmail.com ou 21-2721 4685)
5. obs(String. Campo não obrigatório de texto para colocar quaisquer observações necessárias.)

Recursos:
1. `/`: `GET`(lista todos os contatos)
2. `/`: `POST`(adiciona um contato)
3. `/<int:id>`:`GET`(Visualiza dados de um registro)
4. `/<int:id>`:`PUT`(Atualiza um registro)
5. `/<int:id>`:`DELETE`(Apaga um registro)
___

## Passo a passo para instalação, teste e inicialização:
___

### Instalação do Python:
1. Instalar python através do site `https://www.python.org/downloads/`
2. Prosseguir com instruções sobre instalação. Obs: marcar, se possível, a opção de adicionar python ao PATH.
---
### Instalação do programa
1. Extrair arquivos do .zip ou `git clone https://github.com/xFelipe/Agenda.git`
2. Acessar a pasta do projeto
3. Abrir terminal na pasta atual
4. `python3 -m venv venv`
5. Ativar VENV: Linux: `source venv/bin/activate` | Windows: `venv\Scripts\activate`
6. Instalar dependências com comando: `pip install -r requirements.txt`
7. Realizar testes: `python manage.py test`
8. Realizar migrações com comando `python manage.py migrate`
9. Iniciar servidor: `python manage.py runserver`
10. Acesse em seu navegador o endereço: `localhost:8000`
obs: Se quiser testar manualmente, apague a linha 49 do arquivo `agenda/settings.py`, salve o arquivo e volte ao passo 9.
