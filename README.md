# FastAPI Notes API

## Descrição
Este projeto é uma API criada com **FastAPI** e persistência no banco de dados **MySQL** para gerenciar notas pessoais.

## Funcionalidades

- **Listar Notas** (GET `/notes`)
- **Criar Nota** (POST `/notes`)
- **Atualizar Nota** (PUT `/notes/{id}`)
- **Excluir Nota** (DELETE `/notes/{id}`)

## Tecnologias Utilizadas

- **FastAPI** (framework backend)
- **SQLAlchemy** (ORM para manipulação do banco de dados)
- **MySQL** (banco de dados relacional)
- **Pydantic** (validação de dados)

## Requisitos para Execução

- **Python 3.9+**
- **MySQL** (com um banco de dados criado)

### Pacotes Necessários

Instale os pacotes listados no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Configuração do Projeto

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/daviddaniel2025/api_remember-app.git
   cd api_remember-app
   ```

2. **Configuração do Banco de Dados**

   Certifique-se de que o MySQL está instalado e configurado corretamente. Crie o banco de dados:

   ```sql
   CREATE DATABASE notes;
   ```

3. **Configure a String de Conexão**

   No arquivo `database.py`, atualize a variável `DATABASE_URL` com suas credenciais do MySQL:

   ```python
   DATABASE_URL = "mysql+pymysql://username:password@localhost:3306/notes_db"
   ```

   Substitua `username`, `password`, e `localhost` pelos valores correspondentes ao seu ambiente local.

4. **Inicie o Banco de Dados**

   Rode o seguinte comando para criar as tabelas no banco:

   ```bash
   python main.py
   ```

## Como Rodar a API em Localhost

1. **Inicie o Servidor FastAPI**

   Rode o servidor com o `uvicorn`:

   ```bash
   uvicorn main:app --reload
   ```

   O servidor estará rodando em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Exemplos de Requisições

### Criar uma Nota (POST `/notes`)

```json
{
  "title": "Reunião",
  "description": "Reunião com a equipe de desenvolvimento",
  "event_date": "2024-12-22"
}
```

### Listar Notas (GET `/notes`)

Resposta:

```json
[
  {
    "id": 1,
    "title": "Reunião",
    "description": "Reunião com a equipe de desenvolvimento",
    "event_date": "2024-12-22"
  }
]
```

### Atualizar Nota (PUT `/notes/{id}`)

```json
{
  "title": "Reunião Atualizada",
  "description": "Novo horário para a reunião",
  "event_date": "2024-12-22"
}
```

### Excluir Nota (DELETE `/notes/{id}`)

Resposta:

```json
{"message": "Nota excluída com sucesso."}
```

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

