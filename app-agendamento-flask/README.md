# 📅 Projeto 06/10: Aplicação de Agendamento/Reservas (Full-Stack)

## ✨ Visão Geral do Projeto

Este projeto é uma aplicação **Full-Stack** que simula um sistema de agendamento de consultas para uma clínica. Ele é uma evolução do conceito CRUD, adicionando a complexidade de gerenciar **relacionamentos entre tabelas** e **validação de tempo/conflitos**.

O foco principal foi garantir que as regras de negócio de agendamento (como horários no futuro e a prevenção de sobreposições) fossem gerenciadas de forma robusta no Back-End.

---

## 🛠️ Stack Tecnológica

| Camada | Tecnologia | Propósito |
| :--- | :--- | :--- |
| **Back-End (Framework)** | **Python (Flask)** | Gerenciamento de rotas, validação de dados e lógica de agendamento. |
| **Banco de Dados** | **SQLite (via Flask-SQLAlchemy)** | Persistência de dados com **Relacionamento One-to-Many** (Um Paciente tem muitas Consultas). |
| **Front-End** | **HTML5 & CSS3, Jinja2** | Interface de usuário para entrada de dados de agendamento e visualização da lista. |

---

## 🚀 Funcionalidades e Regras de Negócio

* **Agendamento de Consultas:** O usuário pode preencher seus dados, data, hora e motivo da consulta.
* **Modelos Relacionados:** O sistema usa duas tabelas (`Paciente` e `Consulta`) interligadas por uma Chave Estrangeira (`paciente_id`).
* **Validação Crítica de Horário:**
    1.  **Horário Futuro:** Impede o agendamento de consultas para datas e horas que já passaram.
    2.  **Prevenção de Conflito:** Garante que apenas uma consulta seja agendada por horário (simulando um único recurso, como um médico).
* **Controle de Status:** Implementação da funcionalidade de **Cancelamento** para alterar o status da consulta de "Agendada" para "Cancelada".
* **Mensagens Flash:** Uso de mensagens (sucesso ou erro) para dar feedback imediato ao usuário após submissão do formulário.

---

## ⚙️ Como Executar Localmente

1.  **Clone e Configure:**
    ```bash
    git clone [https://github.com/IsraelCassute/06-app-agendamento-flask.git](https://github.com/IsraelCassute/06-app-agendamento-flask.git)
    cd 06-app-agendamento-flask
    
    # Ative seu ambiente virtual (venv)
    pip install Flask Flask-SQLAlchemy
    ```

2.  **Execute o Servidor:**
    ```bash
    python app.py
    ```

3.  **Acesse:** `http://127.0.0.1:5000/`

### 🧪 Teste de Conflito:

Tente agendar duas consultas diferentes (mesmo paciente ou paciente diferente) para a **mesma data e hora exata**. O Back-End deve impedir o segundo agendamento e retornar uma mensagem de erro ao Front-End.

---

## 👤 Desenvolvedor

**Israel Cassute** | Desenvolvedor na TheCodeMinds | Luanda, Angola

## 🤝 Conexão e Comunidade

Se você tiver dúvidas sobre os projetos ou as tecnologias, sinta-se à vontade para entrar em contato.

* **LinkedIn:** [https://www.linkedin.com/in/israel-cassute/](https://www.linkedin.com/in/israel-cassute/)
* **Twitter/X:** [https://x.com/Israzuba0023](https://x.com/Israzuba0023)
* **Instagram:** [https://www.instagram.com/israzuba0023/](https://www.instagram.com/israzuba0023/)
