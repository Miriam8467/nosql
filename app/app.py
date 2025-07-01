import streamlit as st
from pymongo import MongoClient
from bson.objectid import ObjectId

# Conectar ao MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["eshop"]
colecao = db["clientes"]

st.set_page_config(page_title="E-Shop Brasil", layout="wide")
st.title("🛒 Gestão de Clientes - E-Shop Brasil")

# Menu lateral
menu = st.sidebar.selectbox("Menu", ["Criar", "Visualizar", "Atualizar", "Deletar"])

# Criar
if menu == "Criar":
    st.subheader("Cadastrar novo cliente")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    telefone = st.text_input("Telefone")
    cpf = st.text_input("CPF")
    
    if st.button("Salvar"):
        colecao.insert_one({
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "cpf": cpf
        })
        st.success("Cliente cadastrado com sucesso!")

# Visualizar
elif menu == "Visualizar":
    st.subheader("Lista de Clientes")
    dados = list(colecao.find().limit(100))
    for cliente in dados:
        st.markdown(f"**{cliente.get('nome')}** - {cliente.get('email')} - CPF: {cliente.get('cpf')}")

# Atualizar
elif menu == "Atualizar":
    st.subheader("Atualizar Cliente")
    clientes = list(colecao.find().limit(100))
    cliente_selecionado = st.selectbox("Escolha um cliente", clientes, format_func=lambda x: x.get("nome", ""))
    
    if cliente_selecionado:
        novo_nome = st.text_input("Novo nome", cliente_selecionado.get("nome"))
        novo_email = st.text_input("Novo email", cliente_selecionado.get("email"))
        novo_telefone = st.text_input("Novo telefone", cliente_selecionado.get("telefone"))

        if st.button("Atualizar"):
            colecao.update_one(
                {"_id": cliente_selecionado["_id"]},
                {"$set": {
                    "nome": novo_nome,
                    "email": novo_email,
                    "telefone": novo_telefone
                }}
            )
            st.success("Cliente atualizado com sucesso!")

# Deletar
elif menu == "Deletar":
    st.subheader("Excluir Cliente")
    clientes = list(colecao.find().limit(100))
    cliente_selecionado = st.selectbox("Selecione um cliente para deletar", clientes, format_func=lambda x: x.get("nome", ""))

    if st.button("Excluir"):
        colecao.delete_one({"_id": cliente_selecionado["_id"]})
        st.success("Cliente deletado com sucesso!")

