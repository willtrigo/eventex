# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/willtrigo/eventex.svg?branch=master)](https://travis-ci.org/willtrigo/eventex)
[![Code Health](https://landscape.io/github/willtrigo/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/willtrigo/eventex/master)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. ative o virtualenv
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:willtrigo/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env-sample
python manage.py testes
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEGUB=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```
