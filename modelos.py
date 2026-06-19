from conexao import conectar

class Produto:

    def __init__(self, nome, preco, categoria, ativo=True, id=None, criado_em=None):
        self.id = id
        self.nome =  nome
        self.preco = preco
        self.categoria = categoria
        self.ativo = ativo
        self.criado_em = criado_em

    def exibir(self):
        texto = f"""
        Código: {self.id}
        Nome: {self.nome}
        Preco: {self.nome}
        Categoria: {self.categoria}
        Ativo: {self.ativo}
        Criado em: {self.criado_em}
        """
        print(texto)    

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "INSERT INTO produto (nome, preco, categoria, ativo) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (self.nome, self.preco, self.categoria, self.ativo))

        conexao.comit()
        conexao.close()

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM produto"        
    cursor.execute(sql)

    produtos = []
    for id, nome, preco, categoria, ativo, criado_em in cursor.fetchall():
        produto = Produto(nome, preco, categoria, ativo, id, criado_em)
        produtos.append(produto)
        
    conexao.close()
    return produtos