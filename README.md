# Sistema de Gestão de Estoque

## Descrição
Este projeto é um sistema de gestão de estoque que permite a administração de produtos, controle de estoque e geração de relatórios. Ele é construído utilizando uma arquitetura de microserviços com Python e FastAPI.

## Estrutura do Projeto
O projeto está dividido em três microserviços principais:

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
- Pytest

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
    - O product-service estará rodando em http://localhost:8000.
    - O stock-service e report-service estarão rodando em suas respectivas portas configuradas no docker-compose.yml.

## Tecnologias Utilizadas
Para executar os testes, execute o seguinte comando:

    pytest

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