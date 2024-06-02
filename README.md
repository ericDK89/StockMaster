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

### Pré-requisitos
Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.

### Passos para Configuração

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/ericDK89/inventory-management.git
   cd inventory-management
