from acesso_cep import BuscaEndereco

cep = "07845020"
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro,cidade,uf)