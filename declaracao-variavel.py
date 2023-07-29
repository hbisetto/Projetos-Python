idade: int
salario: float; altura: float
genero: str
nome: str
dadosconf: bool
#a especificação dos tipos de variável é opcional em Python. Ou seja, essas primeiras cinco linhas não são necessárias para o código rodar

idade = 20
salario = 5800.5
altura = 1.68
genero = "F"
nome = "Maria Silva"
dadosconf = True


print(f"IDADE = {idade}")
print(f"SALARIO = {salario:.2f}") 
# ":.2f" Para duas casas decimais, no caso
print(f"ALTURA = {altura:.2f}")
print(f"GENERO = {genero}")
print(f"NOME = {nome}")
print(f"DADOS CORRETOS = {dadosconf}")
#Testando as opções de saída de dados
print(idade)
print(f"Idade = {idade}")
