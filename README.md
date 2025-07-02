# E-Shop Brasil – Integração de Soluções NoSQL com Streamlit

Este projeto foi desenvolvido para a disciplina de **Banco de Dados Avançado e Big Data**, com foco na construção de uma aplicação completa que integra **MongoDB**, **Streamlit** e **Docker**, permitindo operações CRUD sobre uma base de dados de clientes.

## Objetivo

O objetivo do projeto é modernizar a gestão de dados da empresa fictícia **E-Shop Brasil**, utilizando tecnologias NoSQL e criando uma interface web para manipulação interativa das informações dos clientes.

---

## Tecnologias Utilizadas

- **MongoDB** (Banco de dados NoSQL)
- **Streamlit** (Framework para construção de aplicações web em Python)
- **Docker & Docker Compose** (Containerização e orquestração de serviços)
- **Python 3.11**
- **Faker** (Geração de dados fictícios)
- **TQDM** (Barra de progresso para inserção de dados)

---

## Estrutura do Projeto

eshop-nosql/
│
├── app/ # Aplicação CRUD com Streamlit
│ └── app.py
│
├── data/ # Script de geração de dados
│ └── gerar_dados.py
│
├── Dockerfile # Imagem da aplicação Streamlit
├── docker-compose.yml # Orquestração do MongoDB e da aplicação
├── requirements.txt # Bibliotecas Python usadas no projeto
└── README.md # Este arquivo


---

## Como Executar o Projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/Miriam8467/nosql.git
cd eshop-nosql

## 2. Construindo containers

docker-compose up --build

## 3. Acessar a aplicação no navegador
A aplicação estará disponível em:
http://localhost:8501

O MongoDB estará rodando na porta padrão: 27017.

## 4. Geração de Dados com Faker
O script gerar_dados.py insere dados simulados no MongoDB. Para gerar os dados:

python data/gerar_dados.py

Ele gera mais de 1 milhão de registros de clientes com nome, e-mail, CPF e telefone.

## 5. Funcionalidades da Aplicação
Criar clientes com nome, e-mail, telefone e CPF

Visualizar registros existentes no MongoDB

Atualizar dados (exceto o CPF)

Deletar registros da base
