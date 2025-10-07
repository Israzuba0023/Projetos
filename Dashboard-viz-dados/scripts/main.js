const API_URL = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false';

// FUNÇÃO DE MELHORIA: Formata números grandes para M (Milhões), B (Bilhões), T (Trilhões)
function formatLargeNumber(num) {
    if (num >= 1.0e+12) {
        return (num / 1.0e+12).toFixed(2) + " T";
    }
    if (num >= 1.0e+9) {
        return (num / 1.0e+9).toFixed(2) + " B";
    }
    if (num >= 1.0e+6) {
        return (num / 1.0e+6).toFixed(2) + " M";
    }
    return num.toLocaleString('en-US');
}

async function fetchData() {
    // 1. GESTÃO DO SPINNER
    const loadingOverlay = document.getElementById('loading-overlay');
    loadingOverlay.classList.remove('hidden');

    try {
        console.log("Buscando dados da API CoinGecko...");

        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Erro HTTP! Status: ${response.status}`);
        }
        const data = await response.json();

        // 2. PROCESSAMENTO DE DADOS
        const top5 = data.slice(0, 5); // Para os gráficos

        // Dados para Gráfico de Barras (Preço Atual)
        const labelsBar = top5.map(coin => coin.symbol.toUpperCase());
        const dataBar = top5.map(coin => coin.current_price);

        // Dados para Gráfico de Rosca (Variação 24h)
        const labelsPie = top5.map(coin => coin.name);
        // Usamos o Math.abs para garantir que a porcentagem negativa não atrapalhe a visualização do Rosca
        const dataPie = top5.map(coin => Math.abs(coin.price_change_percentage_24h.toFixed(2)));

        // 3. ATUALIZA OS CARTÕES DE RESUMO
        const totalCap = data.reduce((sum, coin) => sum + coin.market_cap, 0);

        document.getElementById('total-moedas').textContent = `${data.length} Tipos`;

        // Aplica a formatação de números grandes
        document.getElementById('cap-total').textContent = `$${formatLargeNumber(totalCap)}`;

        // 4. RENDERIZA OS GRÁFICOS
        renderBarChart(labelsBar, dataBar);
        renderPieChart(labelsPie, dataPie);

    } catch (error) {
        console.error("Erro ao buscar ou processar dados:", error);
        // Exibe erro na UI
        document.querySelector('.dashboard-container').innerHTML =
            `<h2 style="color: red; text-align: center; margin-top: 50px;">
                Não foi possível carregar os dados. Verifique a API ou sua conexão.
            </h2>`;
    } finally {
        // Oculta o spinner no final, independentemente do sucesso ou falha
        loadingOverlay.classList.add('hidden');
    }
}


// ===============================================
// FUNÇÕES DE RENDERIZAÇÃO COM CHART.JS
// ===============================================

function renderBarChart(labels, data) {
    const ctx = document.getElementById('barChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Preço Atual (USD)',
                data: data,
                backgroundColor: 'rgba(0, 123, 255, 0.7)',
                borderColor: 'rgba(0, 123, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false } // Oculta a legenda para Barras simples
            },
            scales: {
                y: {
                    beginAtZero: false,
                    title: { display: true, text: 'Preço (USD)' }
                }
            }
        }
    });
}

function renderPieChart(labels, data) {
    const ctx = document.getElementById('pieChart').getContext('2d');
    // Cores dinâmicas para melhor visualização
    const backgroundColors = [
        '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'
    ];

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: backgroundColors,
                hoverBackgroundColor: backgroundColors
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'bottom' }
            }
        }
    });
}

// Executa a função principal
fetchData();