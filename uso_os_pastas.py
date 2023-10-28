import os

os.chdir('./PastaScript')

r = input("Qual o nome da pasta a ser criada? ")
print(r)

os.mkdir(r)
os.chdir(r)

pastas = {'Pasta Documentos', 'Pasta Imagens', 'Pasta Vídeos'}

for pasta in pastas:
    os.mkdir(pasta)
    
todos =  os.listdir()
print(f'Pastas criadas: {todos}')



# os.cd(f'./{r}')

# todos = os.listdir()
# 
# pasta_raiz = os.getcwd()
# print(pasta_raiz)
# 
# for cadaUm in todos:
    # os.chdir(f'{cadaUm}')
    # os.mkdir('NovoArquivo--')
    # print(f'Pasta "Novo arquivo" criada em {cadaUm}')
    # os.chdir(pasta_raiz)
    # 
# print('Processo completo!')
