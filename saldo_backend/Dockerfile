# Use a imagem oficial do Python como imagem base
FROM python:3.10

# Defina o diretório de trabalho no contêiner
WORKDIR /app


# Copie o arquivo requirements.txt para o contêiner e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos do projeto para o contêiner
COPY . .

# Exponha a porta que o Gunicorn usará
EXPOSE 8000

# Execute o Gunicorn com o aplicativo WSGI do Django
CMD ["gunicorn", "saldo_backend.wsgi:application", "--bind", "0.0.0.0:8000"]