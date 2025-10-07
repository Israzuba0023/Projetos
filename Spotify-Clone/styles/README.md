# 🎵 Projeto 02/10: Spotify Clone (Web Player UI)

## ✨ Visão Geral do Projeto

Este projeto é um clone fiel (apenas Front-End) da interface de usuário (UI) do **Spotify Web Player/Desktop App**. O objetivo principal foi demonstrar o domínio de técnicas avançadas de layout em CSS e a adição de interatividade básica via JavaScript puro.

Foi um exercício focado em **fidelidade visual**, **responsividade** e organização de código Front-End para criar uma experiência complexa de múltiplos painéis. 

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído puramente com tecnologias Front-End vanilla, para garantir o máximo controle sobre o layout e a manipulação do DOM.

* **HTML5:** Estrutura semântica para os três painéis principais (Sidebar, Conteúdo, Player).
* **CSS3:** Utilização intensiva de **CSS Grid** e **Flexbox** para o layout principal. Includes variáveis CSS para um esquema de cores coeso.
* **JavaScript (ES6+):** Adiciona interatividade básica e manipulação do DOM.
* **Font Awesome:** Utilizado para os ícones de navegação e controles de mídia.

---

## 🚀 Funcionalidades Demonstradas

Este clone demonstra o domínio das seguintes habilidades de Front-End:

1.  **Layout Multi-Painel Complexo:** Uso de **CSS Grid** para criar a estrutura não trivial de Sidebar Fixo, Player Fixo e Conteúdo Rolável.
2.  **Responsividade Avançada (Media Queries):** O layout se adapta a três tamanhos de tela (Desktop, Tablet e Mobile), demonstrando:
    * **Compactação da Sidebar** (Tablet).
    * **Ocultação e Toggle da Sidebar** via botão de menu (Mobile).
3.  **Interatividade JS Pura:**
    * **Toggle Play/Pause:** Altera o ícone de Play para Pause (e vice-versa) ao clicar.
    * **Toggle Favorito:** Altera o ícone de coração (vazado para preenchido) e sua cor para a cor de destaque do Spotify (`--color-green`).
4.  **Fidelidade ao Design:** Recriação cuidadosa de elementos como cartões de playlist, barra de progresso e controles de usuário.

---

## 💡 Como Executar Localmente (Para Estudantes)

Este projeto não requer um servidor Back-End.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/IsraelCassute/02-spotify-clone-ui.git](https://github.com/IsraelCassute/02-spotify-clone-ui.git)
    ```
2.  **Navegue até o Diretório:**
    ```bash
    cd 02-spotify-clone
    ```
3.  **Abra:** Simplesmente abra o arquivo `index.html` em seu navegador.

### ⚠️ Nota para o Estudante:

Observe como o arquivo `styles/main.css` utiliza o **`grid-template-areas`** e as **Media Queries** para lidar com os diferentes tamanhos de tela. Tente simular a tela do celular (largura menor que 600px) e veja como o JavaScript interage com o botão de menu.

---

## ✍️ Próximos Passos (Potenciais Melhorias)

* [ ] Implementar um componente de *Scroll Shadow* no cabeçalho do conteúdo principal.
* [ ] Usar um framework de componentes Front-End (ex: React) para refatorar os cartões de playlist.
* [ ] Adicionar lógica de **simulação de carregamento de dados** via JS para o conteúdo principal.

---

## 👤 Desenvolvedor

**Israel Cassute** | Desenvolvedor na TheCodeMinds | Luanda, Angola

* **LinkedIn:** [https://www.linkedin.com/in/israel-cassute/](https://www.linkedin.com/in/israel-cassute/)
