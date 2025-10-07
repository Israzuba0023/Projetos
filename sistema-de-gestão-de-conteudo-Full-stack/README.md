# ✍️ Projeto : Blog Simples (CMS Full-Stack)

## ✨ Visão Geral do Projeto

Este projeto é um **Sistema de Gestão de Conteúdo (CMS)** básico para um blog. Ele demonstra o desenvolvimento de um aplicativo Full-Stack onde as operações **CRUD** são integradas diretamente nas rotas do servidor, gerando HTML dinâmico.

Diferente do Projeto 4 (que era uma API pura), o Projeto 5 foca na **Renderização Dinâmica de Templates** (`Jinja2` via Flask) e na separação de **Visualização Pública** (Front-End para leitores) e **Ações de Administração** (Back-End para criação/edição).

---

## 🛠️ Stack Tecnológica

| Camada | Tecnologia | Propósito |
| :--- | :--- | :--- |
| **Back-End (Framework)** | **Python (Flask)** | Gerenciamento de rotas, lógica de CRUD e renderização de templates. |
| **Templates** | **Jinja2 (em Flask)** | Injeção de dados do Python no HTML para renderizar páginas dinâmicas. |
| **Banco de Dados** | **SQLite (via Flask-SQLAlchemy)** | Persistência de dados para os posts do blog (título, corpo, data). |
| **Front-End** | **HTML5 & CSS3** | Estrutura e estilização da interface pública e do painel de administração. |

---

## 🚀 Funcionalidades Chave

* **CRUD Completo de Posts:** Criação, leitura, edição e exclusão de posts de blog.
* **Rotas Separadas:** Separação clara entre a rota pública (`/`, `/post/<id>`) e a rota administrativa (`/admin`).
* **Renderização Dinâmica:** O Front-End é gerado dinamicamente no Back-End (Server-Side Rendering), buscando os dados do banco antes de enviar o HTML ao cliente.
* **Formulários de Administração:** Utilização de formulários HTML simples (`POST`) para interagir com o Back-End, sem a necessidade de JavaScript complexo (diferente do Projeto 4).

---

## ⚙️ Como Executar Localmente

1.  **Clone e Configure:**
    ```bash
    git clone [https://github.com/IsraelCassute/05-cms-simples-flask.git](https://github.com/IsraelCassute/05-cms-simples-flask.git)
    cd 05-cms-simples-flask
    
    # Ative seu ambiente virtual (venv)
    # Ex: source venv/bin/activate
    
    pip install Flask Flask-SQLAlchemy
    ```

2.  **Execute o Servidor:**
    ```bash
    python app.py
    ```

3.  **Acesse:**
    * **Início do Blog:** `http://127.0.0.1:5000/`
    * **Painel Admin:** `http://127.0.0.1:5000/admin` (Comece aqui para criar posts!)

---

## 👤 Desenvolvedor

**Israel Cassute** | Desenvolvedor na TheCodeMinds | Luanda, Angola

## 🤝 Conexão e Comunidade

Se você tiver dúvidas sobre os projetos ou as tecnologias, sinta-se à vontade para entrar em contato.

* **LinkedIn:** [https://www.linkedin.com/in/israel-cassute/](https://www.linkedin.com/in/israel-cassute/)
* **Twitter/X:** [https://x.com/Israzuba0023](https://x.com/Israzuba0023)
* **Instagram:** [https://www.instagram.com/israzuba0023/](https://www.instagram.com/israzuba0023/)

