# 🍔 Sistema de Gerenciamento de Delivery (Estilo iFood)

Este projeto é uma aplicação **CRUD (Create, Read, Update, Delete)** desenvolvida em **Python** e integrada ao banco de dados NoSQL **MongoDB Atlas**. A aplicação simula o gerenciamento de cardápio e produtos de um e-commerce de delivery de comida.

## 📌 Funcionalidades

* **Create (Cadastrar):** Adiciona novos pratos ao cardápio (nome, restaurante, categoria, preço e disponibilidade).
* **Read (Consultar e Filtrar):**
  * Listagem completa de todos os itens cadastrados.
  * Filtro por categoria (busca *case-insensitive* usando `$regex`).
  * Filtro por faixa de preço máximo (operador `$lte`).
* **Update (Atualizar):** Altera nome, preço e status de disponibilidade de um prato existente utilizando seu `ObjectId`.
* **Delete (Excluir):** Remove um registro do banco de dados pelo seu ID.

## 🛠️ Tecnologias e Bibliotecas

* **Linguagem:** Python 3
* **Banco de Dados:** MongoDB Atlas (Nuvem)
* **Bibliotecas Utilizadas:**
  * `pymongo` - Driver oficial do MongoDB para conexão e manipulação dos dados em Python.
  * `dnspython` - Necessário para suporte a conexões de clusters MongoDB no formato `mongodb+srv://`.

## 🗂️ Estrutura do Documento JSON (MongoDB)

Os registros são salvos na coleção `cardapio` dentro do banco de dados `ifood_db`:

```json
{
  "_id": { "$oid": "65f1a2b3c4d5e6f7a8b9c0d1" },
  "nome": "Hambúrguer Artesanal",
  "restaurante": "Burger House",
  "categoria": "Lanches",
  "preco": 32.50,
  "disponivel": true
}
```

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.8 ou superior instalado.
* Cluster configurado no MongoDB Atlas.

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instalar as Dependências
Execute no terminal:
```bash
pip install pymongo dnspython
```

### 3. Configurar Conexão e Executar
Abra o arquivo `main.py` e insira sua Connection String do MongoDB Atlas na variável `MONGO_URI`:

```python
MONGO_URI = "mongodb+srv://<usuario>:<senha>@cluster...mongodb.net/?retryWrites=true&w=majority"
```

Em seguida, rode a aplicação:
```bash
python main.py
```

## 📋 Menu da Aplicação

```text
==============================
   SISTEMA DE DELIVERY  
==============================
1. Cadastrar novo prato
2. Consultar cardápio / Filtros
3. Atualizar prato
4. Excluir prato
5. Sair
```
