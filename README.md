# Ecommerce Order Service

Este é um microsserviço de gerenciamento de pedidos para um sistema de e-commerce, desenvolvido em Python utilizando Flask e SQLAlchemy.

## Requisitos

- Python 3.10
- Docker
- PostgreSQL
- pip

## Como Executar

1. **Suba o container do PostgreSQL:**

   ```bash
   docker run --name ecommerce_postgres -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=ecommerce_db -p 5432:5432 -d postgres
    ```

2. **Construa e rode o container da Aplicação**

    ```bash
    docker build -t ecommerce_order_service .
    docker run --name ecommerce_order_service -p 5000:5000 --link ecommerce_postgres:postgres -d ecommerce_order_service
    ```

3. Inicie a Aplicação:

    ```bash
    python -m app.main
    ```

4. Acesse a API em:

    ```bash
    http://localhost:5000/api/orders
    ```

## Testes

1. Para rodar os testes automatizados, execute:

    ```bash
    pytest
    ```

## Rotas da API

- `POST` /api/orders: Cria um novo pedido.
- `GET` /api/orders: Lista todos os pedidos.
- `GET` /api/orders/{id}: Retorna detalhes de um pedido específico.
- `PUT` /api/orders/{id}: Atualiza um pedido específico.
- `DELETE` /api/orders/{id}: Deleta um pedido específico.