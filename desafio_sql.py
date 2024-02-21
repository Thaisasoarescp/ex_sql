import sqlite3
conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#CRIANDO A TABELA E ADICIONANDO ALUNOS

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(50))')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Marcos Roberto", 19, "Tecnologia da Informação")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Janaina Silva", 18, "Ciência de dados")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Simone Vitti", 26, "Engenharia da Computação")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Flávia Sampaio", 30, "Ciência da Computação")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Sílvio Campestre", 19, "Análise e desenvolvimento de sistemas")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(6, "Mayara Cardoso", 45, "Engenharia de Telecomunicações")')

#CONSULTAS SQL

#dados = cursor.execute('SELECT * FROM alunos')
#for alunos in dados:
    #print(alunos)

#dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
#for alunos in dados:
    #print(alunos)

#Selecionar estudantes de engenharia em ordem alfabética
#dados = cursor.execute('SELECT nome FROM alunos WHERE curso LIKE "%Engenharia%" GROUP BY nome')
#for alunos in dados:
 #   print(alunos)

#Contar nomero total de alunos da tabela
#dados = cursor.execute('SELECT COUNT (id) FROM alunos')
#for id in dados:
 #   print(id)

#Atualizar a idade de um aluno específico da tabela
#dados = cursor.execute('UPDATE alunos SET idade = 30 WHERE nome = "Janaina Silva"')

#Remova um aluno pelo seu ID
#dados = cursor.execute('DELETE FROM alunos WHERE id = 5')


#cursor.execute("CREATE TABLE 'clientes' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'nome' VARCHAR(100), 'idade' INT, 'saldo' FLOAT )")

# cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, 'Carolina Cardoso', 35, 1500.00)")
# cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, 'Fabio Lauro', 48, 16000.00)")
# cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, 'Silmara Reget', 40, 30000.00)")
# cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, 'Gilberto Sampaio', 26, 1200.00)")
# cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, 'Kleber Calixto', 35, 100.00)")
# cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES(6, 'Priscila Sort', 22, 1500.00)")

# dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
# for clientes in dados:
#     print(clientes)

#Fazendo a média dos saldos
# dados = cursor.execute("SELECT AVG (saldo) FROM clientes")
# for saldo in dados:
#   print(saldo)

#Saldo Máximo
# dados = cursor.execute("SELECT MAX (saldo) FROM clientes")
# for saldo in dados:
#    print(saldo)

#Quantos clientes com saldo acima de 1000.00
# dados = cursor.execute("SELECT COUNT (saldo) FROM clientes WHERE saldo > 1000.0")
# for saldo in dados:
#    print(saldo)

#Atualizando dados
# cursor.execute("UPDATE clientes SET saldo = 200000.0 WHERE nome = 'Silmara Reget' ")


#Removendo cliente pelo id
#cursor.execute("DELETE FROM clientes WHERE id = 1")

#Junção de tabelas
#cursor.execute("CREATE TABLE 'compras' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , 'produto' VARCHAR(100), 'valor' FLOAT )")
#cursor.execute('ALTER TABLE compras ADD COLUMN cliente_id INTEGER REFERENCES clientes(id)')


conexao.commit()
conexao.close