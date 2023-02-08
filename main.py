# Instalar 3 bibliotecas, Pandas, Twilio e Openpyx

# Para cada arquivo: Janeiro, Fevereiro, Março, Abril, Maio e Junho

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada
import pandas as pd

Lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']
for mes in Lista_meses:
    tabela_venda = pd.read_excel (f'{mes}.xlsx')
    if (tabela_venda['Vendas'] > 55000).any():
        vendedor = tabela_venda.loc[tabela_venda['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_venda.loc[tabela_venda['Vendas'] > 55000,'Vendas'].values[0]
        print (f'No mês de {mes}, o vendedor {vendedor}, bateu a marca de {vendas} e ganhou o benefício')

#Primeiramente, criei um array chamado lista_meses, depois, criei uma estrutura de repetição para passar cada mês um a um.
#Após isso, criei uma variavel para receber esses valores, se chama tabela_venda, essa varíavel precisa da biblioteca pandas, que abreviei para pd para funcionar e do método read_excel.
#apos isso, verifico se existe qualquer valor na coluna vendas das planilhas maior que 55000, se tiver, cria-se uma variável vendedor e uma vendas, que receberá o nome do vendedor e o valor das vendas respctivamente.
#para saber qual linha da planilha tem um valor maior que 55000, eu uso o método loc(linha,coluna), para localizar a linha.!Importante, o Método Loc retorna uma tabela como resultado,
#então é necessário usar o values[0], para retornar somente o valor. Após isso, basta printar o resultado.
