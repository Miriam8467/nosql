# data/gerar_dados.py

from faker import Faker
from pymongo import MongoClient
from tqdm import tqdm

fake = Faker('pt_BR')

# Conexão com o MongoDB (ajuste a URL se necessário)
client = MongoClient("mongodb://localhost:27017/")
db = client["eshop"]
colecao = db["clientes"]

# Número de registros a gerar
quantidade = 1_000_000

def gerar_cliente():
    return {
        "nome": fake.name(),
        "email": fake.email(),
        "telefone": fake.phone_number(),
        "cpf": fake.cpf(),
        "endereco": {
            "rua": fake.street_name(),
            "numero": fake.building_number(),
            "cidade": fake.city(),
            "estado": fake.estado_sigla(),
            "cep": fake.postcode()
        },
        "criado_em": fake.date_time_this_decade()
    }

# Inserção em lotes para desempenho
batch_size = 1000
clientes_batch = []

for i in tqdm(range(quantidade)):
    cliente = gerar_cliente()
    clientes_batch.append(cliente)

    if len(clientes_batch) == batch_size:
        colecao.insert_many(clientes_batch)
        clientes_batch = []

# Insere o restante
if clientes_batch:
    colecao.insert_many(clientes_batch)

print("Inserção finalizada com sucesso.")
