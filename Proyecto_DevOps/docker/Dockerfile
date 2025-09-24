# -----------------------------
# Imagen base Python
# -----------------------------
FROM python:3.11-slim

# -----------------------------
# Configuración básica del entorno
# -----------------------------

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# -----------------------------
# Directorio de trabajo en el contenedor
# -----------------------------
    
WORKDIR /app

# -----------------------------
# Copiar el código fuente al contenedor
# -----------------------------

COPY ./src/ ./src/

# -----------------------------
# Punto de entrada del contenedor
# -----------------------------

ENTRYPOINT ["python", "src/organizer.py"]