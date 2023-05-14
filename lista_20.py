# Use um dicionário para armazenar informações sobre uma pessoa que você conheça.
# Armazene seu primeiro nome, o sobrenome, a idade e a cidade em que ela vive.
# Você deverá ter chaves como primeiro_nome, sobrenome, idade, e cidade.
# Por fim, mostre cada informação armazenada em seu dicionário.

pessoa = {'primeiro_nome': 'Lucas', 'sobrenome': 'Eduardo', 'idade': 27, 'cidade': 'João Pessoa'}
for chave in pessoa.keys():
    print(f'{chave} : {pessoa[chave]}')
