import math
lista = list ()

numero =0
while (numero!=-1):
    numero = int(input())
    if (numero!=-1):
        lista.append(numero)


soma =0
for i in lista:
    soma+=i

media = soma/len(lista)

maior = lista[0]
for i in lista:
    if (maior<i):
        maior=i


menor = lista[0]
for i in lista:
    if (menor>i):
        menor=i

qtd_maior_media=0
for i in lista:
    if(i > media):
        qtd_maior_media +=1

        

print("A quantidade de números na lista: {}".format(len(lista)))
print("A soma dos números da lista: {}".format(soma))
print("A média considerando os valores na lista: {}".format(media))
print("O maior número da lista: {}".format(maior))
print("O menor número da lista: {}".format(menor))
print("Quantos números da lista são maiores que a média: {}".format(qtd_maior_media))

