salario1: float; salario2: float
nome1: str; nome2: str
idade: int
sexo: str

nome1 = input('Nome da primeira pessoa:')
salario1 = float(input('Salario da primeira pessoa:'))

nome2 = input('Nome da segunda pessoa:')
salario2 = float(input('Salario da segunda pessoa:'))

idade = int(input('Digite uma idade: '))
sexo = str(input('Digite o sexo [M/F]:'))

print(f'Nome1 = {nome1}')
print(f'Salário1 = {salario1}')
print(f'Nome2 = {nome2}')
print(f'Salário2 = {salario2}')
print(f'Idade = {idade}')
print(f'Sexo = {sexo}')
