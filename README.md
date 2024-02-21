# FakePinterest

Este projeto é uma aplicação web chamada FakePinterest, que permite aos usuários se cadastrar, fazer login, postar e visualizar imagens em um feed.
O projeto foi baseado no minicurso Criação de Sites em Python da Hashtag Treinamentos podendo ser encontrado no link abaixo.
[Minicurso Criação de Sites em Python](https://blp.hashtagtreinamentos.com/python/minicurso/criacao-sites-python)

# Configuração e Execução do Projeto

1. Pré-requisitos:

Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo em Python.org.

2. Clone o repositório:

Você pode clonar este repositório usando o Git. No terminal, navegue até a pasta onde deseja clonar o repositório e execute o seguinte comando:
```
bash
git clone https://github.com/seuusuario/FakePinterest.git
```
3. Criação do Ambiente Virtual e Ativação(venv)

Navegue até a pasta FakePinterest onde você clonou o repositório.
Execute o seguinte comando para criar.ativar o ambiente virtual

```
python -m venv venv
```
Execute o seguinte comando para ativar o ambiente virtual
```
venv\Scripts\activate.bat
```

4. Instalação das Dependências:

Navegue até a pasta FakePinterest onde você clonou o repositório.
Execute o seguinte comando para instalar as dependências listadas no arquivo requirements.txt:
```
bash
pip install -r requirements.txt
```

5. Configuração do Ambiente:

Secret Key
Abra a pasta com os arquivos e rode o arquivo "secret.py" para gerar a sua chave secreta aleatória (SECRET_KEY). 
Após, copie a chave gerada e cole ela no arquivo "__init__.py" onde está escrito "SUA SECRET KEY AQUI!" 

Banco de Dados:

O projeto utiliza um banco de dados SQLite, que deve ser criado rodando o arquivo "criar_banco.py".

6. Executando o Aplicativo:

Abra um terminal na pasta do projeto.
Em seguida rode o arquivo "main.py"
no app.run() o parametro "debug=True" está sendo usado para que as alterações sejam refletidas em tempo real (após salvar as mudanças e atualizar a pagina F5)
No proprio terminal irá aparecer um link o qual irá redirecionar para o site que está rodando localmente.
O servidor Flask será iniciado e estará disponível em http://localhost:5000 por padrão.

7. Acessando o Aplicativo:

Abra um navegador da web e acesse http://localhost:5000.
Agora você pode navegar pelo aplicativo, fazer login, cadastrar-se, postar e visualizar imagens no feed.

Observações:

Certifique-se de que as pastas static/fotos_posts existam e tenham as permissões corretas para salvar as imagens postadas.
Este é um guia básico para configurar e executar o aplicativo.

Conclusão:

Com estas etapas, você deve ser capaz de configurar e executar o FakePinterest em sua máquina local. Sinta-se à vontade para explorar e personalizar o projeto de acordo com suas necessidades.
A pasta To-Do possui um arquivo txt com ideias que serão implementadas no futuro.
