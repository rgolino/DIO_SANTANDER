# 🏬 Store API

API RESTful para gerenciamento de produtos de uma loja, desenvolvida com **FastAPI**, **MongoDB** e **TDD com Pytest**. Ideal para fins educativos.

---

## 🚀 Tecnologias Utilizadas
- FastAPI
- Pydantic
- Pytest
- MongoDB + Motor
- Docker & Docker Compose
- Poetry (gerenciador de dependências)

---

## 📦 Funcionalidades
- ✅ Cadastro de produtos
- 🔍 Consulta de produto por ID
- ✏️ Atualização parcial de produto
- 🗑️ Exclusão de produto
- 🔎 Filtros por preço na listagem

---

## 📁 Estrutura do Projeto
```
store_api/
├── database/           # Conexão com o MongoDB
├── models/             # Schemas Pydantic
├── routes/             # Endpoints FastAPI
├── usecases/           # Lógica de negócio
├── tests/              # Testes Pytest
├── main.py             # App FastAPI principal
├── Dockerfile
├── docker-compose.yml
├── Makefile            # Comandos automatizados
└── docs/API_DOCUMENTATION.md
```

---

## ⚙️ Instalação e Execução

### 1. Pré-requisitos
- Docker e Docker Compose

### 2. Clonar o projeto
```bash
git clone https://github.com/rgolino/store_api.git
cd store_api
```

### 3. Subir o ambiente com Docker
```bash
make up
```

### 4. Acessar a documentação da API
```
http://localhost:8000/docs
```

---

## 🧪 Rodar Testes
```bash
make test
```

---

## 📚 Documentação da API
A documentação completa dos endpoints está disponível em:
```
docs/API_DOCUMENTATION.md
```

---

## 🧰 Comandos Úteis via Makefile
| Comando        | Ação                               |
|----------------|------------------------------------|
| `make up`      | Sobe a aplicação com Docker        |
| `make down`    | Para e remove os containers        |
| `make test`    | Executa os testes com pytest       |
| `make logs`    | Mostra os logs da aplicação        |
| `make mongo`   | Abre o shell do MongoDB            |
| `make restart` | Reinicia a aplicação               |

---

## 🧑‍💻 Autor
**Renato Golino**  
Projeto com fins educacionais — TDD na prática com FastAPI.

---

## 📄 Licença
Este projeto está sob a licença MIT.
