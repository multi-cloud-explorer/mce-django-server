# Multi-Cloud Explorer Server

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/multi-cloud-explorer/mce-django-server.svg)](https://travis-ci.org/multi-cloud-explorer/mce-django-server)
[![Coverage Status](https://coveralls.io/repos/multi-cloud-explorer/mce-django-server/badge.svg?branch=master&service=github)](https://coveralls.io/github/multi-cloud-explorer/mce-django-server?branch=master)
[![Code Health](https://landscape.io/github/multi-cloud-explorer/mce-django-server/master/landscape.svg?style=flat)](https://landscape.io/github/multi-cloud-explorer/mce-django-server/master)

[Documentation](https://multi-cloud-explorer.readthedocs.org)

## Fonctionnalités

- [x] Inventaire automatique des resources
- [x] Historisation des changements au format [Json Patch](http://jsonpatch.com/)
- [ ] WebServices pour recevoir des changements
- [ ] Push des évènements vers une queue de donnée ou un WebHook

## Providers implémentés

- [x] Azure
- [ ] AWS
- [ ] GCP
- [ ] VMware

## Intégre les packages

- [mce-django-app](https://github.com/multi-cloud-explorer/mce-django-app.git)
- [mce-tasks-djq](https://github.com/multi-cloud-explorer/mce-tasks-djq.git)
- [mce-lib-azure](https://github.com/multi-cloud-explorer/mce-lib-azure.git)

## Installation avec docker-compose

```shell

git clone https://github.com/multi-cloud-explorer/mce-django-server.git
cd mce-django-server

export COMPOSE_FILE=docker-compose.yml:docker-compose.prod.yml
docker-compose up -d --build

# Vérifiez l'état des services
docker-compose ps

# Creez le compte administrateur
docker-compose exec app ./manage.py createsuperuser --username admin --email admin@localhost.net

# Récupérer le login/password de l'administrateur
docker-compose logs app --tail 10
```


