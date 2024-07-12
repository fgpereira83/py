f=open("meuArquivo.txt","rt")
# print(f.read())
#print(f.readline())
#print(f.readline())


for linha in f:
    print(linha)

f.close()