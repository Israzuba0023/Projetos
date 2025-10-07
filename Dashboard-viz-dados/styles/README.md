# 📈 Projeto 03/10: Dashboard de Visualização de Criptomoedas

## ✨ Visão Geral do Projeto

Este projeto consiste em um **Dashboard** de Front-End para buscar, processar e visualizar dados de criptomoedas em tempo real. O foco principal foi a integração com uma **API externa** e o uso de uma **biblioteca de gráficos** para transformar dados brutos em insights visuais.

Este projeto demonstra habilidades cruciais para qualquer projeto de análise, relatório ou Business Intelligence.

---

## 🛠️ Tecnologias Utilizadas

* **HTML5 & CSS3:** Para a estrutura limpa e o layout do dashboard (Grid e Flexbox).
* **JavaScript (ES6+):** Motor principal para consumo de API, manipulação de dados e DOM.
* **`fetch()` API:** Utilizada para buscar dados em formato JSON da API CoinGecko.
* **Chart.js:** Biblioteca JavaScript leve e popular para renderização de gráficos.

---

## 🚀 Funcionalidades Chave

1.  **Consumo de API Externa:** Busca de dados de preços, capitalização e variação de mercado da **CoinGecko API**.
2.  **Visualização de Dados (Chart.js):** Renderização de dois tipos de gráficos (Barras e Rosca) para apresentar o preço e a variação percentual em 24h.
3.  **UX Profissional:**
    * **Spinner de Carregamento:** Exibe um *spinner* enquanto a API busca os dados, melhorando a experiência do usuário.
    * **Formatação de Números Grandes:** Função JS dedicada para formatar valores de capitalização de mercado em unidades como **B (Bilhões)** ou **T (Trilhões)**, garantindo legibilidade.
4.  **Tratamento de Erros:** Implementação de um bloco `try...catch...finally` para gerenciar falhas de conexão ou na API, informando o usuário e escondendo o spinner.

---

## 💡 Como Executar Localmente

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/IsraelCassute/03-dashboard-viz-dados.git](https://github.com/IsraelCassute/03-dashboard-viz-dados.git)
    ```
2.  **Abra o Arquivo:**
    Abra o arquivo `index.html` em seu navegador. (Não é necessário um servidor local, mas é necessário conexão com a internet para acessar a API).

### 📝 Notas para Estudantes:

* Observe a função **`formatLargeNumber(num)`** no `main.js`. Esta é uma técnica valiosa para relatórios financeiros.
* O bloco **`try...catch...finally`** é a melhor prática para lidar com chamadas assíncronas de API no JavaScript.

---

## 👤 Desenvolvedor

**Israel Cassute** | Desenvolvedor na TheCodeMinds | Luanda, Angola
