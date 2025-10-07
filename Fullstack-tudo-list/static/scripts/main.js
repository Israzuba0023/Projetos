const API_URL = '/api/tarefas';
const taskForm = document.getElementById('task-form');
const taskInput = document.getElementById('task-input');
const taskList = document.getElementById('task-list');
const statusMessage = document.getElementById('status-message');

// =======================================================
// RENDERIZAÇÃO E EVENTOS DO DOM
// =======================================================

// Cria o elemento <li> para uma tarefa individual
function createTaskElement(task) {
    const listItem = document.createElement('li');
    listItem.classList.add('task-item');
    if (task.concluida) {
        listItem.classList.add('completed');
    }

    listItem.setAttribute('data-id', task.id);

    // Descrição (usada para o toggle de conclusão)
    const descriptionSpan = document.createElement('span');
    descriptionSpan.classList.add('task-description');
    descriptionSpan.textContent = task.descricao;
    descriptionSpan.addEventListener('click', () => toggleTask(task.id, !task.concluida));

    // Botão de Excluir
    const deleteBtn = document.createElement('button');
    deleteBtn.classList.add('btn', 'delete-btn');
    deleteBtn.textContent = 'X';
    deleteBtn.addEventListener('click', () => deleteTask(task.id));

    listItem.appendChild(descriptionSpan);
    listItem.appendChild(deleteBtn);

    return listItem;
}

// Renderiza todas as tarefas na lista
function renderTasks(tasks) {
    taskList.innerHTML = '';
    if (tasks.length === 0) {
        statusMessage.textContent = "Nenhuma tarefa pendente! Adicione uma.";
    } else {
        statusMessage.textContent = "";
        tasks.forEach(task => {
            taskList.appendChild(createTaskElement(task));
        });
    }
}

// =======================================================
// COMUNICAÇÃO COM A API (CRUD)
// =======================================================

// READ: Buscar todas as tarefas
async function fetchTasks() {
    try {
        const response = await fetch(API_URL);
        const tasks = await response.json();
        renderTasks(tasks);
    } catch (error) {
        console.error("Erro ao buscar tarefas:", error);
        statusMessage.textContent = "Erro ao carregar tarefas. Tente novamente.";
    }
}

// CREATE: Adicionar nova tarefa
taskForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const description = taskInput.value.trim();
    if (!description) return;

    try {
        await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ descricao: description })
        });

        taskInput.value = ''; // Limpa o input
        await fetchTasks(); // Recarrega a lista
    } catch (error) {
        console.error("Erro ao criar tarefa:", error);
    }
});

// UPDATE: Marcar/Desmarcar como concluída
async function toggleTask(id, isCompleted) {
    try {
        await fetch(`${API_URL}/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ concluida: isCompleted })
        });
        await fetchTasks(); // Recarrega para refletir a mudança
    } catch (error) {
        console.error("Erro ao atualizar tarefa:", error);
    }
}

// DELETE: Excluir tarefa
async function deleteTask(id) {
    if (!confirm('Tem certeza que deseja excluir esta tarefa?')) return;

    try {
        await fetch(`${API_URL}/${id}`, {
            method: 'DELETE'
        });
        await fetchTasks(); // Recarrega para remover o item
    } catch (error) {
        console.error("Erro ao excluir tarefa:", error);
    }
}

// Inicia o aplicativo buscando as tarefas ao carregar
fetchTasks();