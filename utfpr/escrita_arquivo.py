f=open("meuArquivo.txt","w")

for i in range(10):
    f.write(">> {}".format(i))
f.close()

f=open("meuArquivo.txt","rt")
#f=open("meuArquivo.txt")
print(f.read())
f.close()