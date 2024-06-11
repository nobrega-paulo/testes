arquivo = open("C:/Users/pnobr/Documents/estudos/testes/python/fazendo_dio/manipulação de arquivos/teste.txt", "w")
arquivo.write("Escrevendo dados em um novo aquivo.")
arquivo.writelines(["\n", "escrevendo ", "\n", "um ","\n" , "novo ", "\n", "texto."])
arquivo.close()