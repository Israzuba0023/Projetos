document.addEventListener('DOMContentLoaded', () => {

    const playButton = document.querySelector('.large-icon');
    const favoriteIcon = document.getElementById('favorite-toggle');
    const menuToggleBtn = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');

    // ===============================================
    // AÇÃO 1: Alternar Play/Pause no Player Fixo
    // ===============================================
    if (playButton) {
        playButton.addEventListener('click', () => {
            if (playButton.classList.contains('fa-play-circle')) {
                // Mudar para PAUSE
                playButton.classList.remove('fa-play-circle');
                playButton.classList.add('fa-pause-circle');
                console.log("Música: PLAY (Pausar é a próxima ação)");
            } else {
                // Mudar para PLAY
                playButton.classList.remove('fa-pause-circle');
                playButton.classList.add('fa-play-circle');
                console.log("Música: PAUSE (Play é a próxima ação)");
            }
        });
    }

    // ===============================================
    // AÇÃO 2: Mudar a Cor e o Estado de Favorito
    // ===============================================
    if (favoriteIcon) {
        favoriteIcon.addEventListener('click', () => {
            // Verifica se o ícone é "far" (regular/vazado)
            if (favoriteIcon.classList.contains('far')) {
                // Adiciona Favorito (Ícone sólido e cor verde)
                favoriteIcon.classList.remove('far');
                favoriteIcon.classList.add('fas', 'favorited');
                console.log("Música adicionada aos favoritos.");
            } else {
                // Remove Favorito (Ícone vazado e cor padrão)
                favoriteIcon.classList.remove('fas', 'favorited');
                favoriteIcon.classList.add('far');
                console.log("Música removida dos favoritos.");
            }
        });
    }

    // ===============================================
    // AÇÃO 3: Mostrar/Esconder a Sidebar em Telas Pequenas (Menu Toggle)
    // ===============================================
    if (menuToggleBtn && sidebar) {
        menuToggleBtn.addEventListener('click', (e) => {
            // Previne que o clique afete outros elementos (ex: o main content)
            e.stopPropagation();
            // Alterna a classe 'active' que controla a translação no CSS
            sidebar.classList.toggle('active');
            console.log("Sidebar: Alternada (Mobile).");
        });
    }

    // Fechar Sidebar ao clicar fora dela em Mobile (Melhoria de UX)
    document.querySelector('#main-content').addEventListener('click', () => {
        if (window.innerWidth <= 600 && sidebar.classList.contains('active')) {
            sidebar.classList.remove('active');
        }
    });

});