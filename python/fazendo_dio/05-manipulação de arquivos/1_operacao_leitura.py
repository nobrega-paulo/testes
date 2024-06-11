arquivo = open(
    "C:/Users/pnobr/Documents/estudos/testes/python/fazendo_dio/manipulação de arquivos/lorem.txt", "r"
    )
print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())
# while len (linha := arquivo.readline()):
 #   print(linha)
arquivo.close()