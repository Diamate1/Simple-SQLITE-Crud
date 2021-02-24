from crud import *

# Escolhendo o banco de dados
DB = crud('alunos.db')

# Criar a primeira tabela
'''
DB.CREATE_TABLE('alunos', 'nome varchar(255), sobrenome varchar(255)')
'''

# Inserir dados
'''
DB.INSERT_INTO('alunos', ['teste1', 'testesobrenome1'])
DB.INSERT_INTO('alunos', ['teste2', 'testesobrenome2'])
DB.INSERT_INTO('alunos', ['teste3', 'testesobrenome3'])
'''

# Visualizar dados
'''
result = DB.SELECT('alunos', '*')
print(result)
result = DB.SELECT('alunos', '*', where={'coluna': 'nome', 'oper': '=', 'valor': 'teste1'})
print(result)
'''

# Atualizar dados
'''
result = DB.SELECT('alunos', '*')
print(result)
DB.UPDATE('alunos', {'coluna': 'nome', 'oper': '=', 'valor': 'batata'}, {'coluna': 'nome', 'oper': '=', 'valor': 'teste2'})
result = DB.SELECT('alunos', '*')
print(result)
'''

# Deletar dados
'''
DB.DELETE('alunos', where={'coluna': 'nome', 'oper': '=', 'valor': 'teste3'})
'''

# Apagar tabela
'''
DB.DROP_TABLE('alunos')
'''

DB.conn.close()