# StockMaster

## Descrição
Este projeto é um sistema de gestão de estoque que permite a administração de produtos, controle de estoque e geração de relatórios. Ele é construído utilizando uma arquitetura de microserviços com Python e FastAPI.

## Estrutura do Projeto
O projeto está dividido em quatro microserviços principais:

- **gateway-service**: Centraliza as requisições dos serviços em uma única porta.
- **product-service:** Gerencia os produtos no estoque.
- **stock-service:** Controla a quantidade de produtos em estoque.
- **report-service:** Gera relatórios sobre o estoque.

Cada serviço possui sua própria configuração, modelo de dados e rotas.

## Tecnologias Utilizadas
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose
- Pandas

## Configuração e Execução

### Passos para Configuração

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/ericDK89/inventory-management.git
   cd inventory-management
   ```

2. **Crie o arquivo `.env` em cada diretório de serviço (product-service, stock service, report-service):**
   ```bash
    POSTGRES_USER=your_username
    POSTGRES_PASSWORD=your_password
    POSTGRES_DB=your_database
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
     ```
      
3. **Construa e inicie os serviços usando Docker Compose:**
    ```bash
    docker-compose up --build
     ```

4. **Acesse a aplicação:**
    - O gateway-service estará rodando em http://localhost:8000.
    - O product-service, stock-service e report-service estarão rodando em suas respectivas portas configuradas no docker-compose.yml.


## Endpoints

### Product Service
- **POST** /products
    - Cria um novo produto.
    
- **GET** /products
    - Recupera uma lista de produtos.

- **GET** /products/{product_id}
    - Recupera um produto específico pelo ID.

- **PUT** /products/{product_id}
    - Atualiza um produto pelo ID.

- **DELETE** /products/{product_id}
    - Deleta um produto pelo ID.

### Stock Service
- **PUT** /stock/{product_id}
    - Atualizar o estoque de um produto específico pelo ID.

- **GET** /stock/{product_id}
    - Consultar o estoque de um produto específico pelo ID.

### Report Service
- **POST** /reports/sales
    - Gerar um relatório de vendas.

- **POST** /reports/inventory
    - Gerar um relatório de estoque.

---

# Inventory Management System

## Description
This project is an inventory management system that allows for the administration of products, stock control, and report generation. It is built using a microservices architecture with Python and FastAPI.

## Project Structure
The project is divided into three main microservices:

- **product-service**: Manages the products in the inventory.
- **stock-service:**: Controls the quantity of products in stock.
- **report-service:**: Generates reports on the inventory.

Each service has its own configuration, data model, and routes.

## Technologies Used
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose
- Pandas

## Setup and Execution

### Setup Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ericDK89/inventory-management.git
   cd inventory-management
   ```

2. **Create the .env file in each service directory (product-service, stock-service, report-service):**
   ```bash
    POSTGRES_USER=your_username
    POSTGRES_PASSWORD=your_password
    POSTGRES_DB=your_database
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
     ```
      
3. **Build and start the services using Docker Compose:**
    ```bash
    docker-compose up --build
     ```

4. **Access the application:**
    - The gateway-service will be running at http://localhost:8000.
    - The product-service, stock-service, and report-service will be running on their respective ports configured in the docker-compose.yml.

## Endpoints

### Product Service
- **POST** /products
    - Create a new product.

- **GET** /products
    - Retrieve a list of products.

- **GET** /products/{product_id}
    - Retrieve a specific product by ID.

- **PUT** /products/{product_id}
    - Update a product by ID.

- **DELETE** /products/{product_id}
    - Delete a product by ID.

### Stock Service
- **PUT** /stock/{product_id}
    - Update the stock of a specific product by ID.

- **GET** /stock/{product_id}
    - Retrieve the stock of a specific product by ID.

### Report Service
- **POST** /reports/sales
    - Generate a sales report.

- **POST** /reports/inventory
    - Generate an inventory report.
