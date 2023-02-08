# Instalar 3 bibliotecas, Pandas, Twilio e Openpyx

# Para cada arquivo: Janeiro, Fevereiro, Março, Abril, Maio e Junho

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada
import pandas as pd

Lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']
for mes in Lista_meses:
    print(mes)
    tabela_venda = pd.read_excel (mes +'.xlsx')
    print (tabela_venda)
