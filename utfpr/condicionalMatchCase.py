opcao = int(input("Digite uma opcao"))

match opcao:
    case 1:
        print("Falar com atendente")
    case 2:
        print("Duvidas frequentes")
    case _:
        print("opção invalida")



response=400
match response:
    case 400 | 401 |403:
        print("Erro")
    case 200:
        print("Sucesso")
    case _:
        print("Código desconhecido")