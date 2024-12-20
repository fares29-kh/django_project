# Utilisation de l'image Python officielle comme image de base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installer les dépendances à partir de requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application Django dans le conteneur
COPY . .

# Exposer le port 8000 (port par défaut de Django)
EXPOSE 8000

# Commande pour lancer l'application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
