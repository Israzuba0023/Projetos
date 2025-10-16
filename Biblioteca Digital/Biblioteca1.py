# Importações necessárias
import tkinter as tk  # Biblioteca para criar interfaces gráficas
from tkinter import filedialog, messagebox  # Ferramentas para abrir arquivos e exibir mensagens
import os  # Módulo para interagir com o sistema operacional (ex.: verificar arquivos)
import json  # Módulo para trabalhar com arquivos JSON (salvar e carregar dados)
from PyPDF2 import PdfReader  # Biblioteca para ler arquivos PDF

# Classe principal da aplicação
class BibliotecaDigital:
    def __init__(self, root):
        # Configurações iniciais da janela principal
        self.root = root  # A janela principal da aplicação
        self.root.title("Biblioteca Digital")  # Define o título da janela
        self.root.geometry("800x600")  # Define o tamanho da janela (largura x altura)
        self.root.configure(bg="#FFD7B5")  # Define a cor de fundo da janela (laranja claro)

        # Caminho do arquivo JSON para armazenar os livros
        self.arquivo_livros = "livros.json"  # Nome do arquivo onde os livros serão salvos

        # Carrega os livros salvos no arquivo JSON
        self.livros = self.carregar_livros()  # Lê os livros salvos e os coloca no dicionário `self.livros`

        self.usuario_logado = False  # Variável para controlar se o usuário está logado

        # Inicia a tela de login
        self.tela_login()  # Chama o método que cria a tela de login

    def carregar_livros(self):
        """Carrega os livros salvos no arquivo JSON."""
        if os.path.exists(self.arquivo_livros):  # Verifica se o arquivo JSON existe
            with open(self.arquivo_livros, "r", encoding="utf-8") as arquivo:  # Abre o arquivo em modo de leitura
                return json.load(arquivo)  # Carrega os dados do arquivo JSON como um dicionário
        return {}  # Se o arquivo não existir, retorna um dicionário vazio

    def salvar_livros(self):
        """Salva os livros no arquivo JSON."""
        with open(self.arquivo_livros, "w", encoding="utf-8") as arquivo:  # Abre o arquivo em modo de escrita
            json.dump(self.livros, arquivo, ensure_ascii=False, indent=4)  # Salva o dicionário `self.livros` no arquivo

    def tela_login(self):
        """Cria a tela de login."""
        self.limpar_tela()  # Limpa a tela para exibir apenas os widgets da tela de login

        # Cria um rótulo com o título "Login"
        tk.Label(self.root, text="Login", font=("Arial", 24), bg="#FFD7B5").pack(pady=20)

        # Cria um rótulo para o campo de entrada do usuário
        tk.Label(self.root, text="Usuário:", bg="#FFD7B5").pack()

        # Cria um campo de entrada para o nome de usuário
        self.usuario_entry = tk.Entry(self.root, width=30)  # Campo de texto para digitar o usuário
        self.usuario_entry.pack(pady=5)  # Adiciona o campo à interface com um espaçamento

        # Cria um rótulo para o campo de entrada da senha
        tk.Label(self.root, text="Senha:", bg="#FFD7B5").pack()

        # Cria um campo de entrada para a senha (os caracteres são ocultados com "*")
        self.senha_entry = tk.Entry(self.root, width=30, show="*")  # Campo de texto para digitar a senha
        self.senha_entry.pack(pady=5)  # Adiciona o campo à interface com um espaçamento

        # Cria um botão para confirmar o login
        tk.Button(self.root, text="Entrar", command=self.verificar_login, bg="#FFA500", fg="white").pack(pady=10)

    def verificar_login(self):
        """Verifica o login do usuário."""
        usuario = self.usuario_entry.get().strip()  # Obtém o nome de usuário digitado e remove espaços extras
        senha = self.senha_entry.get().strip()  # Obtém a senha digitada e remove espaços extras

        # Credenciais fixas para autenticação
        usuario_valido = "20212025"  # Usuário correto
        senha_valida = "0123456789fn"  # Senha correta

        # Verifica se o usuário e a senha estão corretos
        if usuario == usuario_valido and senha == senha_valida:
            self.usuario_logado = True  # Marca o usuário como logado
            self.tela_principal()  # Redireciona para a tela principal
        else:
            # Exibe uma mensagem de erro se as credenciais estiverem incorretas
            messagebox.showerror("Erro de Login", "Usuário ou senha incorretos.")

    def tela_principal(self):
        """Cria a tela principal da biblioteca."""
        self.limpar_tela()  # Limpa a tela para exibir apenas os widgets da tela principal

        # Cria um rótulo com o título "Biblioteca Digital"
        tk.Label(self.root, text="Biblioteca Digital", font=("Arial", 24), bg="#FFD7B5").pack(pady=20)

        # Cria um rótulo para a barra de pesquisa
        tk.Label(self.root, text="Pesquisar Livro:", bg="#FFD7B5").pack()

        # Cria um campo de entrada para pesquisar livros
        self.pesquisa_entry = tk.Entry(self.root, width=40)  # Campo de texto para digitar o termo de pesquisa
        self.pesquisa_entry.pack(pady=5)  # Adiciona o campo à interface com um espaçamento

        # Cria um botão para realizar a pesquisa
        tk.Button(self.root, text="Pesquisar", command=self.pesquisar_livro, bg="#FFA500", fg="white").pack(pady=5)

        # Cria uma área de texto para listar os livros
        self.lista_livros_text = tk.Text(self.root, height=10, width=80, bg="white")  # Área de texto para exibir os livros
        self.lista_livros_text.pack(pady=10)  # Adiciona a área de texto à interface com um espaçamento

        # Cria botões para adicionar, ler e baixar livros
        tk.Button(self.root, text="Adicionar Livro", command=self.adicionar_livro, bg="#FFA500", fg="white").pack(pady=5)
        tk.Button(self.root, text="Ler Livro Selecionado", command=self.ler_livro, bg="#FFA500", fg="white").pack(pady=5)
        tk.Button(self.root, text="Baixar Livro Selecionado", command=self.baixar_livro, bg="#FFA500", fg="white").pack(pady=5)

        # Atualiza a lista de livros na interface
        self.atualizar_lista_livros()  # Chama o método que exibe os livros salvos

    def adicionar_livro(self):
        """Permite ao usuário adicionar um livro ao sistema."""
        arquivo = filedialog.askopenfilename(  # Abre uma janela para selecionar um arquivo
            title="Selecionar Livro",  # Título da janela
            filetypes=[("Arquivos PDF", "*.pdf")]  # Filtra apenas arquivos PDF
        )
        if arquivo:  # Se um arquivo foi selecionado
            nome_livro = os.path.basename(arquivo)  # Obtém o nome do arquivo (sem o caminho completo)
            self.livros[nome_livro] = arquivo  # Adiciona o livro ao dicionário `self.livros`
            self.salvar_livros()  # Salva os livros no arquivo JSON
            self.atualizar_lista_livros()  # Atualiza a lista de livros na interface
            messagebox.showinfo("Sucesso", f"Livro '{nome_livro}' adicionado à biblioteca.")  # Exibe uma mensagem de sucesso

    def atualizar_lista_livros(self):
        """Atualiza a área de texto com a lista de livros."""
        self.lista_livros_text.delete(1.0, tk.END)  # Limpa a área de texto
        for idx, livro in enumerate(self.livros.keys(), start=1):  # Percorre os livros salvos
            self.lista_livros_text.insert(tk.END, f"{idx}. {livro}\n")  # Insere cada livro na área de texto

    def pesquisar_livro(self):
        """Pesquisa livros pelo nome."""
        termo = self.pesquisa_entry.get().strip().lower()  # Obtém o termo de pesquisa e converte para minúsculas
        if not termo:  # Se o campo de pesquisa estiver vazio
            self.atualizar_lista_livros()  # Mostra todos os livros
            return

        # Filtra os livros que contêm o termo pesquisado no nome
        livros_filtrados = {nome: path for nome, path in self.livros.items() if termo in nome.lower()}
        self.lista_livros_text.delete(1.0, tk.END)  # Limpa a área de texto
        if not livros_filtrados:  # Se nenhum livro corresponder ao termo
            self.lista_livros_text.insert(tk.END, "Nenhum livro encontrado.\n")  # Exibe uma mensagem de erro
        else:
            for idx, livro in enumerate(livros_filtrados.keys(), start=1):  # Percorre os livros filtrados
                self.lista_livros_text.insert(tk.END, f"{idx}. {livro}\n")  # Insere cada livro na área de texto

    def ler_livro(self):
        """Abre o livro selecionado para leitura."""
        livro_selecionado = self.obter_livro_selecionado()  # Obtém o caminho do livro selecionado
        if livro_selecionado:  # Se um livro foi selecionado
            try:
                reader = PdfReader(livro_selecionado)  # Lê o arquivo PDF
                texto = "\n".join(page.extract_text() for page in reader.pages)  # Extrai o texto de todas as páginas
                self.mostrar_texto_livro(texto)  # Exibe o texto em uma nova janela
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível ler o livro: {e}")  # Exibe uma mensagem de erro

    def baixar_livro(self):
        """Baixa o livro selecionado para o computador."""
        livro_selecionado = self.obter_livro_selecionado()  # Obtém o caminho do livro selecionado
        if livro_selecionado:  # Se um livro foi selecionado
            destino = filedialog.asksaveasfilename(  # Abre uma janela para salvar o arquivo
                defaultextension=".pdf",  # Define a extensão padrão como .pdf
                filetypes=[("Arquivos PDF", "*.pdf")]  # Filtra apenas arquivos PDF
            )
            if destino:  # Se um destino foi escolhido
                try:
                    with open(livro_selecionado, "rb") as origem, open(destino, "wb") as destino_arquivo:
                        destino_arquivo.write(origem.read())  # Copia o conteúdo do livro para o novo arquivo
                    messagebox.showinfo("Sucesso", "Livro baixado com sucesso!")  # Exibe uma mensagem de sucesso
                except Exception as e:
                    messagebox.showerror("Erro", f"Não foi possível baixar o livro: {e}")  # Exibe uma mensagem de erro

    def obter_livro_selecionado(self):
        """Obtém o caminho do livro selecionado na lista."""
        try:
            indice_selecionado = self.lista_livros_text.index(tk.SEL_FIRST)  # Obtém o índice do texto selecionado
            linha = int(indice_selecionado.split('.')[0]) - 1  # Calcula o número da linha
            nome_livro = list(self.livros.keys())[linha]  # Obtém o nome do livro correspondente à linha
            return self.livros[nome_livro]  # Retorna o caminho do livro
        except tk.TclError:  # Se nenhum livro foi selecionado
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um livro.")  # Exibe uma mensagem de aviso
            return None

    def mostrar_texto_livro(self, texto):
        """Exibe o conteúdo do livro em uma nova janela."""
        janela_leitura = tk.Toplevel(self.root)  # Cria uma nova janela
        janela_leitura.title("Leitura de Livro")  # Define o título da janela
        janela_leitura.geometry("600x400")  # Define o tamanho da janela
        janela_leitura.configure(bg="white")  # Define a cor de fundo da janela (branco)

        texto_livro = tk.Text(janela_leitura, wrap=tk.WORD, bg="white")  # Cria uma área de texto para exibir o conteúdo
        texto_livro.insert(tk.END, texto)  # Insere o texto do livro na área de texto
        texto_livro.pack(expand=True, fill=tk.BOTH)  # Adiciona a área de texto à janela

    def limpar_tela(self):
        """Limpa todos os widgets da tela."""
        for widget in self.root.winfo_children():  # Percorre todos os widgets na janela principal
            widget.destroy()  # Remove cada widget

# Função principal para iniciar a aplicação
if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal
    app = BibliotecaDigital(root)  # Inicializa a aplicação
    root.mainloop()  # Inicia o loop principal da interface gráfica