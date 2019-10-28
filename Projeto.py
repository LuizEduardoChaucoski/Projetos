# Importações
import io
from tkinter import *
import sqlite3

# Globais
conn = sqlite3.connect("cadastro.db")
cursor = conn.cursor()


def criarTabela():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            matricula INTEGER NOT NULL PRIMARY KEY,
            nome TEXT NOT NULL,
            nota TEXT NOT NULL
        );
    """)


criarTabela()

# Definições da Aplicação Principal
principal = Tk()
principal.title("Controle de manutenção de equipamentos")
principal.geometry("1280x720")
principal.resizable(FALSE, FALSE)


# Funções
def adicionar_produto():
    produtos = etProdutos.get()
    nomecliente = etNomeCliente.get()
    status = etStatus.get()
    cursor.execute("""
        INSERT INTO Produtos (Produto, cliente, Status) VALUES (?, ?, ?)""", (produtos, nomecliente, status))
    conn.commit()
    lstProdutos.insert(END, (produtos, nomecliente, status))


def deletar_produto():
    cadastrar_produto = etProdutoDeletar.get()
    cursor.execute("""
        DELETE FROM produtos WHERE cadastrar=?""", (cadastrar_produto,))
    conn.commit()
    lstProdutos.delete(0, END)
    lista = cursor.execute("""
        SELECT * FROM produtos;
        """)
    for i in lista:
        lstProdutos.insert(END, i)


def mudar_status():
    cadastrar_produto = etProdutoMudar.get()
    novo_status = etNovoStatus.get()
    cursor.execute("""
        UPDATE status SET status = ? WHERE produto = ?""", (cadastrar_produto, novo_status))
    conn.commit()
    lstProdutos.delete(0, END)
    lista = cursor.execute("""
        SELECT * FROM produtos;
        """)
    for i in lista:
        lstProdutos.insert(END, i)


def exportar():
    with io.open('cadastro.sql', 'w') as f:
        for linha in conn.iterdump():
            f.write('%s\n' % linha)
    cursor.execute("""
        SELECT * FROM produtos;
    """)
    with io.open('produtos.txt', 'w') as f:
        for linha in cursor.fetchall():
            linha = str(linha)
            f.write('%s\n' % linha)


# Widgets - Principal
lblTitulo = Label(principal, text="Cadastro")
lblProdutoStatus = Label(principal, text="Produto / Cluente / Status")

# Widgets - Adicionar Produto
lblAdicionarProduto = Label(principal, text="Adicionar Produto")
lblProduto = Label(principal, text="Produto: ")
lblNomecliente = Label(principal, text="Nome do cliente: ")
lblStatus = Label(principal, text="Status do produto: ")
etProdutos = Entry(principal)
etNomeCliente = Entry(principal)
etStatus = Entry(principal)
btnAdd = Button(principal, text="Adicionar", command=adicionar_produto())

# Widgets - Deletar Aluno
lblCadastrarProduto = Label(principal, text="Deletar Produto")
lblProdutoDeletar = Label(principal, text="Produto: ")
etProdutoDeletar = Entry(principal, width=10)
btnDel = Button(principal, text="Deletar", command=deletar_produto())

# Widgets - Mudar Nota
lblMudarStatus = Label(principal, text="Mudar Status")
lblStatusMudar = Label(principal, text="Status: ")
lblNovoStatus = Label(principal, text="Status Status: ")
etProdutoMudar = Entry(principal)
etNovoStatus = Entry(principal)
btnMudarStatus = Button(principal, text="Mudar Status", command=mudar_status())

# Widgets - Listar Produtos
scrollbar = Scrollbar(principal)
lstProdutos = Listbox(principal, width=50, height=75)
lstProdutos.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lstProdutos.yview)
lista = cursor.execute("""
    SELECT * FROM produtos;
    """)
for i in lista:
    lstProdutos.insert(END, i)

# Posicionamento de Widgets - Principal #
lblTitulo.place(x=275)
lblNomecliente.place(x=308, y=30)

# Posicionamento de Widgets - Listar Produtos
lstProdutos.place(x=310, y=52)
scrollbar.place()

# Posicionamento de Widgets - Adicionar Produto
lblAdicionarProduto.place(x=100, y=30)
lblProduto.place(x=10, y=52)
etProdutos.place(x=115, y=50)
lblNomecliente.place(x=10, y=82)
etNomeCliente.place(x=115, y=80)
lblStatus.place(x=10, y=112)
etStatus.place(x=115, y=110)
btnAdd.place(x=115, y=145)

# Posicionamento de Widgets - Deletar Produto
lblProdutoDeletar.place(x=100, y=175)
lblProdutoDeletar.place(x=10, y=197)
etProdutoDeletar.place(x=80, y=195)
btnDel.place(x=175, y=198)

# Posicionamento de Widgets - Mudar Status
lblMudarStatus.place(x=105, y=225)
lblAdicionarProduto.place(x=10, y=247)
etProdutoMudar.place(x=115, y=245)
lblNovoStatus.place(x=10, y=277)
etNovoStatus.place(x=115, y=275)
btnMudarStatus.place(x=115, y=308)

principal.mainloop()
