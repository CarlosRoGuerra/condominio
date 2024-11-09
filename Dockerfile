FROM python:3.12-slim

WORKDIR /app

# Instala as dependências do sistema
RUN apt-get update && \
    apt-get install -y \
        gcc \
        python3-dev \
        libpq-dev \
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

# Coleta arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expõe a porta
EXPOSE 8000

# Comando para iniciar
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "your_project.wsgi:application"]
