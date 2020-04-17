# Multi-Cloud Explorer

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/multi-cloud-explorer/mce-django-server.svg)](https://travis-ci.org/multi-cloud-explorer/mce-django-server)
[![Coverage Status](https://coveralls.io/repos/multi-cloud-explorer/mce-django-server/badge.svg?branch=master&service=github)](https://coveralls.io/github/multi-cloud-explorer/mce-django-server?branch=master)
[![Code Health](https://landscape.io/github/multi-cloud-explorer/mce-django-server/master/landscape.svg?style=flat)](https://landscape.io/github/multi-cloud-explorer/mce-django-server/master)
[![Requirements Status](https://requires.io/github/multi-cloud-explorer/mce-django-server/requirements.svg?branch=master)](https://requires.io/github/multi-cloud-explorer/mce-django-server/requirements/?branch=master)

[Documentation sur https://multi-cloud-explorer.readthedocs.org](https://multi-cloud-explorer.readthedocs.org)

## Fonctionnalités

- [ ] Inventaire automatique des resources
  - [x] Azure
  - [ ] AWS
  - [ ] GCP
- [x] Historisation des changements au format [Json Patch](http://jsonpatch.com/)
- [ ] WebServices pour recevoir des changements (ex: EventGrid)
- [ ] Envoi des évènements vers des queues de données (ex: SQS, Redis)

## Fournisseurs implémentés

- [x] Azure
- [ ] AWS
- [ ] GCP

## Packages Multi-Cloud-Explorer intégrés

- [mce-django-app](https://github.com/multi-cloud-explorer/mce-django-app.git)
- [mce-tasks-djq](https://github.com/multi-cloud-explorer/mce-tasks-djq.git)
- [mce-lib-azure](https://github.com/multi-cloud-explorer/mce-lib-azure.git)

## Technologies

- [Python 3.7](https://docs.python.org/fr/3.7/)
- [Django 3](https://docs.djangoproject.com/fr/3.0/)
- [Django-Q](https://django-q.readthedocs.io/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.fr/)
- [Redis](https://redis.io/)
- [Azure SDK](https://github.com/Azure/azure-sdk-for-python)
- [Docker (facultatif)](https://docs.docker.com/get-docker/)

## Installation avec docker-compose

```bash
git clone https://github.com/multi-cloud-explorer/mce-django-server.git
cd mce-django-server

docker-compose up -d

# Vérifiez l'état des services
docker-compose ps

# Créez le compte administrateur
docker-compose exec app ./manage.py createsuperuser \
   --username admin --email admin@localhost.net

# Récupérez le login/password de l'administrateur
docker-compose logs app --tail 10
```

**Ouvrez le navigateur à l'adresse http://127.0.0.1:8000**

### Activation du proxy treafik

> Pour utiliser le proxy treafik, pensez à mettre à jour le label: **traefik.frontend.rule** 
dans **docker-compose.yml** et le password/domain/email dans **traefik/traefik.toml**

```bash
export COMPOSE_FILE=docker-compose.yml:docker-compose.traefik.yml
docker-compose up -d
```

## Installation manuelle

```bash
# Démarrez un serveur PostgreSQL
docker run --name mce-postgres -d \
   -p 127.0.0.1:5432:5432 \
   -e POSTGRES_DB=mce \
   -e POSTGRES_USER=mce \
   -e POSTGRES_PASSWORD=password postgres:12-alpine

# Démarrez un serveur Redis
docker run --name mce-redis -d \
   -p 127.0.0.1:6379:6379 \
   redis:5-alpine redis-server --appendonly yes
```

```bash
git clone https://github.com/multi-cloud-explorer/mce-django-server.git
cd mce-django-server
```

```bash
# Créer un environnement python virtuel
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .[psql]
```

```bash
# Créez un fichier .env
DATABASE_URL=postgres://mce:password@127.0.0.1:5432/mce
CACHE_URL=redis://127.0.0.1:6379/0
DJANGO_SETTINGS_MODULE=mce_django_server.settings.prod
MCE_BIND=0.0.0.0:8000
```

```bash
# Créez les tables SQL
./manage.py migrate

# Créez un compte d'admin
./manage.py createsuperuser --username admin --email admin@localhost.net

# Lancez le serveur web
uvicorn --workers 2 --loop uvloop --proxy-headers --log-level info --host 0.0.0.0 --port 8000 mce_django_server.asgi:application

# Lancez le serveur de tâches dans un autre terminal:
./manage.py rqworker --with-scheduler
```

**Ouvrez le navigateur à l'adresse http://127.0.0.1:8000**

## Roadmap

- Mettre en ligne une version de démonstration
- Terminer l'implémentation AWS/GCP
- Relier les ressources avec une DB Graph
- Intégration de nouveaux providers (vmware/ovh/gandi/...)
- Créer des templates terraform pour générer des ressources de tests
