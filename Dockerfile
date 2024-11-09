# Use uma imagem Python oficial
FROM python:3.9-slim

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho
WORKDIR /app

# Instala as dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia o requirements.txt
COPY requirements.txt .

# Cria e ativa o ambiente virtual, instala as dependências
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o resto do código
COPY . .

# Coleta arquivos estáticos e executa migrações
RUN python manage.py collectstatic --noinput

# Configura o comando para iniciar a aplicação
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Condominio.wsgi:application"]
