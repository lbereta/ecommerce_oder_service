# Dockerfile

# Usando a imagem base oficial do Python
FROM python:3.10-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando o arquivo de requisitos
COPY requirements.txt requirements.txt

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código da aplicação para o diretório de trabalho
COPY . .

# Expondo a porta que o Flask usará
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app/main.py"]
