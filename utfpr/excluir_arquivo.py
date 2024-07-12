# para excluir um arquivo

import os 

if os.path.exists("meuArquivo.txt"):
    os.remove("meuArquivo.txt")
else:
    print("arquivo nao existe")