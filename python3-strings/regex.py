#IMPORTA A BIBLIOTECA RE
import re

email1 = "Meu numero é 91223-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é o meu numero 1234-9098 12238907"

#DEFININDO O PADRAO A SER PROCURADO
padrao = "[0-9]{4,5}[-]*[0-9]{4}"

#FAZ A BUSCA DE ACORDO COM O PADRAO DEFINIDO
#PESQUISA APENAS UM VALOR
#retorno = re.search(padrao,email3)
#PESQUISA TODOS OS VALORES NA STRING
retorno = re.findall(padrao,email3)
#utilizado com a opçao search
#print(retorno.group())
print(retorno)

