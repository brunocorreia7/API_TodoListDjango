# Task Management API

![Python](https://img.shields.io/badge/python-3.x-blue)
![Django](https://img.shields.io/badge/django-4.x-green)
![DRF](https://img.shields.io/badge/django--rest--framework-API-red)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

API REST para **gerenciamento de tarefas** construída com **Django** e **Django REST Framework**.

A aplicação permite que usuários se registrem, façam login e gerenciem suas próprias tarefas utilizando autenticação **JWT**.

---

# Objetivo do Projeto

Este projeto foi desenvolvido para demonstrar a construção de uma **API REST completa com Django**, incluindo:

* autenticação de usuários
* controle de acesso
* CRUD de tarefas
* documentação com Swagger

---

# Tecnologias Utilizadas

* Python
* Django
* Django REST Framework
* SQLite
* JWT (SimpleJWT)
* Swagger (drf-yasg)

---

# Arquitetura da API

A API segue uma arquitetura simples baseada em **REST**.

Cada usuário possui suas próprias tarefas.

```
User
 └── Tasks
       ├── title
       ├── description
       ├── status
       ├── created_at
       └── updated_at
```

---

# Estrutura do Projeto

```
task-api
│
├── config
│   ├── settings.py
│   ├── urls.py
│
├── tasks
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# Modelo de Tarefa

| Campo       | Tipo     | Descrição           |
| ----------- | -------- | ------------------- |
| id          | integer  | Identificador       |
| title       | string   | Título da tarefa    |
| description | string   | Descrição           |
| status      | string   | Status da tarefa    |
| created_at  | datetime | Data de criação     |
| updated_at  | datetime | Data de atualização |

### Status permitidos

```
pending
in_progress
done
```

---

# Regras de Negócio

* Usuário precisa estar autenticado
* Usuário só pode acessar suas próprias tarefas
* Status da tarefa aceita apenas valores definidos
* Datas de criação e atualização são automáticas

---

# Instalação

## 1. Clonar repositório

```
git clone https://github.com/seu-usuario/task-api.git
cd task-api
```

---

## 2. Criar ambiente virtual

```
python -m venv venv
```

Ativar ambiente virtual:

Linux / Mac

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

---

## 3. Instalar dependências

```
pip install -r requirements.txt
```

---

## 4. Executar migrações

```
python manage.py migrate
```

---

## 5. Rodar servidor

```
python manage.py runserver
```

Servidor disponível em:

```
http://127.0.0.1:8000
```

---

# Documentação da API

A documentação interativa está disponível em:

```
/swagger/
```

Exemplo:

```
http://127.0.0.1:8000/swagger/
```

---

# Autenticação

A API utiliza **JWT (JSON Web Token)**.

Após login, será retornado um token `access`.

Esse token deve ser enviado no header das requisições.

```
Authorization: Bearer TOKEN
```

---

# Endpoints

## Autenticação

### Registrar usuário

POST `/api/auth/register`

Exemplo:

```
curl -X POST http://127.0.0.1:8000/api/auth/register \
-H "Content-Type: application/json" \
-d '{
"username":"user",
"password":"123456"
}'
```

---

### Login

POST `/api/auth/login`

```
curl -X POST http://127.0.0.1:8000/api/auth/login \
-H "Content-Type: application/json" \
-d '{
"username":"user",
"password":"123456"
}'
```

Resposta:

```
{
 "refresh": "token",
 "access": "token"
}
```

---

### Usuário autenticado

GET `/api/auth/me`

```
curl http://127.0.0.1:8000/api/auth/me \
-H "Authorization: Bearer TOKEN"
```

---

# Tarefas

## Listar tarefas

GET `/api/tasks`

```
curl http://127.0.0.1:8000/api/tasks \
-H "Authorization: Bearer TOKEN"
```

---

## Criar tarefa

POST `/api/tasks`

```
curl -X POST http://127.0.0.1:8000/api/tasks \
-H "Authorization: Bearer TOKEN" \
-H "Content-Type: application/json" \
-d '{
"title":"Estudar Django",
"description":"Aprender DRF",
"status":"pending"
}'
```

---

## Buscar tarefa por ID

GET `/api/tasks/{id}`

```
curl http://127.0.0.1:8000/api/tasks/1 \
-H "Authorization: Bearer TOKEN"
```

---

## Atualizar tarefa

PUT `/api/tasks/{id}`

```
curl -X PUT http://127.0.0.1:8000/api/tasks/1 \
-H "Authorization: Bearer TOKEN" \
-H "Content-Type: application/json" \
-d '{
"title":"Estudar Django",
"description":"Aprender DRF avançado",
"status":"in_progress"
}'
```

---

## Deletar tarefa

DELETE `/api/tasks/{id}`

```
curl -X DELETE http://127.0.0.1:8000/api/tasks/1 \
-H "Authorization: Bearer TOKEN"
```

---

# Fluxo de Uso da API

1. Criar usuário
2. Fazer login
3. Copiar token `access`
4. Enviar token no header
5. Criar e gerenciar tarefas

---

# Melhorias Futuras

* Paginação
* Filtros por status
* Testes automatizados
* Docker
* PostgreSQL
* CI/CD
* Deploy em cloud

---


