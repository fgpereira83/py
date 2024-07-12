venda1 = {
    'id': 1,
    'items':
    [
        {
            'prodId': 35,
            'descricao': 'Mouse Pad',
            'valor': 49.90
        },
        {
            'prodId': 955,
            'descricao': 'Pendrive',
            'valor': 89.90
        }
    ]
}

venda2 = {
    'id': 2,
    'items':
    [
        {
            'prodId': 4,
            'descricao': 'Teclado QWERTY',
            'valor': 158.50
        },
        {
            'prodId': 88,
            'descricao': 'Caneta',
            'valor': 15.90
        }
    ]
}

venda3 = {
    'id': 3,
    'items':
    [
        {
            'prodId': 8293,
            'descricao': 'Notebook Tabajara',
            'valor': 15890.00
        },
        {
            'prodId': 715,
            'descricao': 'Geforce GTX 450',
            'valor': 627.90
        },
        {
            'prodId': 52,
            'descricao': 'Porta retrato',
            'valor': 29.90
        }
    ]
}

vendas = []
vendas.append(venda1)
vendas.append(venda2)
vendas.append(venda3)
faturamento=0

print("Produtos com valor menor que 50:")
for i in range(len(vendas)):
    items = vendas[i].get("items")
    for j in items:
        dic_item = j
        faturamento += float(dic_item.get("valor"))
        if(float(dic_item.get("valor"))<50):
            print(dic_item.get("descricao"))

print("")
print("Faturamento geral: {0:.2f}".format(faturamento))
