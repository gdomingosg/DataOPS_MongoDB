import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['Avaliacao_DataOPS']

# Dados para o DataFrame
carros = {
    'Carro': ['Onix', 'Polo', 'Sandero', 'Fiesta', 'City'],
    'Cor': ['Prata', 'Branco', 'Prata', 'Vermelho', 'Preto'],
    'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda']
}

montadora = {
    'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda'],
    'Pais': ['EUA', 'Alemanhã', 'França', 'EUA', 'Japão']
}

# Transformando em um DataFrame
df_carros = pd.DataFrame(carros)
df_montadora = pd.DataFrame(montadora)

# Definindo as collection criadas no Mongo
collection_carros = db['Carros']
collection_montadora = db['Montadoras']

# Adicionando os dados nas collection enquanto transforma o DataFrame em um dicionario
collection_carros.insert_many(df_carros.to_dict('records'))
collection_montadora.insert_many(df_montadora.to_dict('records'))

# Fechando a conexão
client.close()
