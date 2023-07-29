#Teste de movimentação de arquivos no Linux via Script no Python
import shutil

shutil.move('aaa.txt', '/[caminho-do-arquivo]/Pasta-destino')
print("Arquivo movido com sucesso.")
