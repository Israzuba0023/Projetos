# 🐍 Projeto : Sistema de Gestão de Tarefas (Full-Stack CRUD)

## ✨ Visão Geral do Projeto

Este projeto é uma aplicação **Full-Stack** completa que implementa todas as operações de **CRUD** (Criar, Ler, Atualizar, Excluir) para uma lista simples de tarefas. Ele serve como uma demonstração fundamental de como conectar um **Front-End** moderno (HTML/CSS/JS) a uma **API RESTful** robusta construída em Python.

Este projeto consolida minha capacidade de trabalhar com as três camadas essenciais do desenvolvimento de software: **Interface**, **Lógica de Aplicação (API)** e **Persistência de Dados**.

---

## 🛠️ Stack Tecnológica

| Camada | Tecnologia | Propósito |
| :--- | :--- | :--- |
| **Back-End (API)** | **Python (Flask)** | Roteamento, criação de endpoints REST e lógica de negócios. |
| **Banco de Dados** | **SQLite (via Flask-SQLAlchemy)** | Persistência de dados para as tarefas. |
| **Front-End (Cliente)** | **HTML5, CSS3, JavaScript** | Interface de usuário limpa e comunicação assíncrona com a API (utilizando `fetch()`). |
| **Dependências** | `Flask`, `Flask-SQLAlchemy` | Pacotes necessários para o ambiente Python. |

---

## 🚀 Funcionalidades da Aplicação

O sistema implementa as seguintes operações na API e na Interface:

| Operação CRUD | Rota da API | Método HTTP | Funcionalidade na UI |
| :--- | :--- | :--- | :--- |
| **CREATE** | `/api/tarefas` | `POST` | Adicionar nova tarefa via formulário. |
| **READ** | `/api/tarefas` | `GET` | Listar todas as tarefas ao carregar a página. |
| **UPDATE** | `/api/tarefas/<id>` | `PUT` | Marcar/desmarcar tarefas como concluídas (clicando na descrição). |
| **DELETE** | `/api/tarefas/<id>` | `DELETE` | Excluir uma tarefa via botão dedicado (`X`). |

---

## 💡 Arquitetura e Fluxo de Dados

O aplicativo segue uma arquitetura cliente-servidor tradicional:

1.  O **Front-End (HTML/JS)** é servido pelo Flask (Rota `/`).
2.  O **JavaScript** atende às interações do usuário (ex: clique no botão "Adicionar").
3.  O JS envia requisições assíncronas (`fetch()`) para os endpoints da API (`/api/tarefas`).
4.  O **Flask** recebe a requisição, interage com o **SQLite** (salva, busca, deleta) e retorna uma resposta JSON.
5.  O JS recebe a resposta JSON e atualiza o DOM da página sem recarregar.

---

## ⚙️ Como Executar Localmente

Siga estas instruções para configurar o ambiente e rodar o aplicativo Full-Stack.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/IsraelCassute/04-fullstack-todo-list.git](https://github.com/IsraelCassute/04-fullstack-todo-list.git)
    cd 04-fullstack-todo-list
    ```

2.  **Crie e Ative o Ambiente Virtual (Recomendado):**
    ```bash
    # Para Linux/macOS
    python3 -m venv venv
    source venv/bin/activate
    # Para Windows (cmd ou PowerShell)
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as Dependências Python:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Isto instalará Flask e Flask-SQLAlchemy)*

4.  **Execute o Servidor Flask:**
    ```bash
    python app.py
    ```
    O servidor estará rodando em `http://127.0.0.1:5000/`.

### ⚠️ Notas de Execução:

* O arquivo `database.db` será criado automaticamente na primeira execução do `app.py`.
* A API está configurada para servir o Front-End (HTML) na rota principal (`/`) e os dados JSON nas rotas `/api/tarefas`.

---

## 👤 Desenvolvedor

**Israel Cassute** | Desenvolvedor na TheCodeMinds | Luanda, Angola

## 🤝 Conexão e Comunidade

Se você tiver dúvidas sobre os projetos ou as tecnologias, sinta-se à vontade para entrar em contato.

* **LinkedIn:** [https://www.linkedin.com/in/israel-cassute/](https://www.linkedin.com/in/israel-cassute/)
* **Twitter/X:** [https://x.com/Israzuba0023](https://x.com/Israzuba0023)
* **Instagram:** [https://www.instagram.com/israzuba0023/](https://www.instagram.com/israzuba0023/)

