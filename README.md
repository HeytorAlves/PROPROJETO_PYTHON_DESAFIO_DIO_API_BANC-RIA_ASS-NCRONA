---

# 💰 Desafio DIO — API Bancária Assíncrona com FastAPI

Este projeto foi desenvolvido como parte do **desafio prático da DIO**, no curso de **Back-end com Python**, com foco na construção e teste de uma **API RESTful assíncrona** utilizando **FastAPI**.

O objetivo foi aplicar conceitos fundamentais de **programação assíncrona**, **persistência de dados**, **boas práticas de API** e **testes**, simulando operações bancárias básicas.

---

## 🎯 Objetivo do Desafio

Construir uma API bancária que permita:

- Criar contas bancárias
- Realizar depósitos
- Realizar saques
- Consultar extrato bancário (statement)
- Manter histórico de transações
- Garantir consistência de saldo

Tudo isso utilizando **operações assíncronas**.

---

## 🧠 Conceitos Trabalhados

- FastAPI com `async/await`
- APIs RESTful
- Programação assíncrona em Python
- Organização em camadas (routes, schemas, store)
- Persistência de dados
- Validação de dados com Pydantic
- Testes e validação via Swagger (OpenAPI)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI**
- **encode/databases**
- **PostgreSQL**
- **Uvicorn**
- **Pydantic**
- **Swagger UI (OpenAPI)**

---

## 📌 Funcionalidades da API

### Criar conta bancária
```http
POST /bank/accounts
````

### Depositar valor

```http
POST /bank/accounts/{account_id}/deposit
```

**Body:**

```json
{
  "amount": 100
}
```

### Sacar valor

```http
POST /bank/accounts/{account_id}/withdraw
```

**Body:**

```json
{
  "amount": 70
}
```

### Consultar extrato bancário

```http
GET /bank/accounts/{account_id}/statement
```

**Exemplo de resposta:**

```json
{
  "account_id": 1,
  "balance": 30,
  "transactions": [
    {
      "id": 3,
      "type": "deposit",
      "amount": 100,
      "created_at": "2026-01-11T17:07:34Z"
    },
    {
      "id": 4,
      "type": "withdraw",
      "amount": 70,
      "created_at": "2026-01-11T17:08:00Z"
    }
  ]
}
```

---

## ▶️ Como Executar o Projeto

### Pré-requisitos

* Python 3.10 ou superior
* PostgreSQL ativo

### Passos

1. Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

2. Acesse a pasta do projeto:

```bash
cd desafio-api-bancaria
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente do banco de dados

5. Execute a aplicação:

```bash
uvicorn main:app --reload
```

6. Acesse a documentação interativa:

```text
http://127.0.0.1:8000/docs
```

---

## ✅ Status do Desafio

✔️ Desafio concluído com sucesso
✔️ Todas as rotas testadas via Swagger
✔️ Saldo e histórico de transações consistentes
✔️ Estrutura alinhada ao padrão exigido pela DIO

---

## 🏁 Considerações Finais

Este projeto consolida o uso do **FastAPI em cenários reais**, reforçando boas práticas no desenvolvimento de APIs assíncronas, além de simular regras de negócio comuns em sistemas financeiros.

Desafio finalizado conforme os requisitos propostos pela **Digital Innovation One (DIO)**.

---
