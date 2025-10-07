// Ativar o scroll suave ao clicar nos links de navegação
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        // Evita o comportamento padrão de salto
        e.preventDefault();

        // Faz o scroll suave para a seção
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Exemplo simples de interação: Adicionar uma classe quando o usuário rolar
window.addEventListener('scroll', () => {
    const header = document.querySelector('.main-header');

    // Se a posição de scroll for maior que 50px
    if (window.scrollY > 50) {
        header.classList.add('scrolled'); // Adiciona uma classe para mudar o estilo
    } else {
        header.classList.remove('scrolled');
    }
});

/*
    Atenção: Para o formulário de contato (contact-form) funcionar, você precisará
    integrá-lo a um serviço de terceiros (como Formspree, Netlify Forms, ou um back-end)
    para realmente enviar o e-mail. O código abaixo é apenas para fins de demonstração/validação básica.
*/
const contactForm = document.getElementById('contact-form');

contactForm.addEventListener('submit', function(e) {
    e.preventDefault();

    // Você faria a validação aqui (ex: verificar se os campos têm o formato correto)
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    if (name && email && message) {
        alert('Mensagem enviada! (No ambiente de produção, este formulário seria processado por um servidor.)');

        // Em um projeto real, você enviaria os dados usando fetch() para um endpoint:
        /*
        fetch('SEU_ENDPOINT_DE_FORMULARIO', {
            method: 'POST',
            body: new FormData(contactForm)
        })
        .then(response => { ... })
        */

        contactForm.reset();
    } else {
        alert('Por favor, preencha todos os campos.');
    }
});