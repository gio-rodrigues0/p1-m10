# Prova 1

Aluno: Giovanna Rodrigues (Aniversariante)

## Como executar:

- É necessário clonar esse repositório na sua máquina.

- Criar e ativar um ambiente virtual de python na raíz do projeto por meio de:

```
python -m venv .
cd Scripts
activate
cd ..
```

- Criar a imagem com o Docker Desktop aberto:

```
docker build -t giovanna0/p1 .
```

- Executar a imagem num container:

```
docker run giovanna0/p1
```

## Arquivos do projeto

- database: Criação do banco de dados

- main.py: Arquivo principal com a API.

- Dockerfile: Conteúdo da imagem.

- Insomnia: Collection de teste do Insomnia.

- requirements.txt: Possui todas as dependências que devem ser baixadas para rodar o projeto.

