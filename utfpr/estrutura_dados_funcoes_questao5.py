#Implemente a função a partir da linha de baixo


n = input("Entre com nome: ")
p = float(input("Entre com peso: "))
a = float(input("Entre com altura: "))

def computeIMC(nome,peso,altura):
    imc = peso/(altura*altura)
    mensagem="{} tem {} kg e {} metros de altura. O seu IMC é {:.2f}".format(nome,peso, altura, imc)
    return mensagem

print(computeIMC(n, p, a))