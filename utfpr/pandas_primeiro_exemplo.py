# importacao do pandas
import pandas

# declaração de um dataset
dados={
    "cliente":["jonas","kim","lucas"],
    "idade":[15,39,68]
}

# conversão dos dados para Dataframe
df = pandas.DataFrame(dados)

print(df)

