hora: int

hora = int(input('Digite uma hora do dia: '))
#A própria indentação é que delimita o limite da estrutura condicional if
if hora < 12:
    print('Bom dia!')
elif hora < 18:
    print('Boa tarde')
else :
    print('Boa noite')

print('Fim do programa')