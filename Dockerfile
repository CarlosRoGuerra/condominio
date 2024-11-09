FROM python:3.12-slim

WORKDIR /app

# Instala as dependências do sistema incluindo MySQL
RUN apt-get update && \
    apt-get install -y \
        gcc \
        python3-dev \
        default-libmysqlclient-dev \
        pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia o projeto
COPY . .

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Remove o comando collectstatic do Dockerfile
# Será executado após o banco de dados estar configurado

# Expõe a porta
EXPOSE 8000

# Comando para iniciar
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn --bind 0.0.0.0:8000 --workers 2 Condominio.wsgi:application"]
