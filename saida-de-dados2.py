#Saída de dados: duas formas
idade : int
salario : float
nome: str
sexo: str

idade = 32
salario = 43543.5
nome = "Maria Silva"
sexo = "F"

#Com interpolação
print(f"A funcionaria {nome}, sexo {sexo}, ganha {salario:.2f}, e tem {idade} anos")

#Com placeholder
print("A funcionaria {:s}, sexo {:s}, ganha {:.2f}, e tem {:d} anos.".format(nome,sexo,salario,idade))
