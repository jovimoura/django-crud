# Django + Python🐍

# Clique e instale o python

[link](https://www.python.org/downloads/release/python-3121/)

# Venv

é uma ferramente q nos ajuda a isolar as dependencias e versoes do projeto, crie uma venv com o comando: 

```markdown
python3 -m venv <nome-da-pasta>
```

Para ativar, entre na pasta e execute:

```markdown
source <nome-da-pasta>/bin/activate
```

Ao ativar o terminal vai ficar assim: 

```markdown
(client1) ➜ django-crud
```

# Instale o Django:

```markdown
pip install Django
```

# Inicie seu projeto:

```markdown
django-admin startproject <nome-do-projeto> .
```

*Obs: o ponto nao permite criar o projeto numa subpasta*

# Execute seu projeto com:

```markdown
python manage.py runserver
```

# Migrate

Execute antes de criar o superuser ou dps de uma migrations

```python
python3 manage.py migrate
```

# Criar superuser

Escolha senha e username dps de executar:

```python
python3 manage.py createsuperuser
```

Apos isso faça o login na rota /admin

# Criando rotas:

Vc pode criar rotas com o comando

```python
python3 manage.py startapp <nome-da-pasta>
```

# Migrations

A cada alteracao ou criacao de novo model, execute:

```python
python3 manage.py makemigrations
```

# Exemplo de código

https://github.com/jovimoura/django-crud

# Título

Texto

- Lista