# Implementar a função validaSenha abaixo:
def validaSenha(password):
    ok = False
    qtd_numeros=0
    qtd_maisculos=0

    # Contenha no mínimo 5 caracteres e no máximo 15 caracteres;
    if len(password) >=5 and len(password)<=15:
        
        for i in password:
           if i in ('0','1','2','3','4','5','6','7','8','9'):
               qtd_numeros +=1
        # Contenha ao menos 2 números entre [0-9];
        if qtd_numeros >=2 :
            for j in password:
                if 'abcdefghijlmnopqrstuvxzwyk'.upper().find(j) != -1 :
                    qtd_maisculos +=1
            if qtd_maisculos >= 2:
                ok = True
    return ok
            



    

#Não alterar o código abaixo
myPass = input()

if (validaSenha(myPass)):
    print("Senha válida")
else:
    print("Senha inválida")