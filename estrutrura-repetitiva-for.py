N = int(input('Quantos números serão digitados?'))

soma = 0

for i in range (0,N):
    #no caso a variável i vai de 0 até um número a menos do que o digitado e lido em N
    x = int(input('Digite um número: '))
    soma = soma + x

print('Soma = ', soma)
print()
print("Caso 2 da estrutura de repetição for com mais parâmetros")

N = int(input('Digite um número: '))
        
for i in range (0, N, 2):
    #Neste caso aqui vai caminhar de dois em dois a partir do i e parando antes do N
    # 0 = valor inicial
    # N = limite
    # 2 =  progressão 2+
    print(i)
