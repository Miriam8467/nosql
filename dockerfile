# Dockerfile

# Usa imagem oficial do Python
FROM python:3.11

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos para dentro do container
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação
COPY ./app ./app

# Comando para iniciar o Streamlit
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
