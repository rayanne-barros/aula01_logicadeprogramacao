mensagem_padrao = 'Você é o convidado especial para a festa'
convidados = ['Harry Potter', 'Herminone', 'Draco']
print(convidados)

# Sabendo que um dos seus convidados não pode participar, adicione ao programa uma mensagem informando que
# ele será retirado da lista, e altere o código para receber um novo personagem. Não esqueça de utilizar
# as funções que te permite adicionar os novos convidados pelo teclado.
print('O convidado Draco não poderá participar e será retirado da lista')
convidados.pop(2)
print(convidados)
print('Rony será seu substituto')
print('Rony ' + mensagem_padrao)
convidados.append('Rony')
print(convidados)

# Adicione a opção de poder adicionar mais pessoas à sua lista.
# i. Uma opção para adicionar um convidado querido ao início da lista;
# ii. Uma convidado no meio da lista;
# iii. E por um convidado ao fim da lista
valor = True
while valor:

    operacao = input('Adicione mais convidados a sua lista: \n 1 -> No ínicio da lista \n 2 -> No meio da lista'
                     ' \n 3 -> No fim da lista \n 4- Fim do programa \n Qual operação deseja realizar?  ')

    if operacao == '1':
        convidados.insert(0, input("Digite o nome do seu convidado: "))
        print(convidados)
    elif operacao == '2':
        convidados.insert(2, input("Digite o nome do seu convidado: "))
        print(convidados)
    elif operacao == '3':
        convidados.append(input("Digite o nome do seu convidado: "))
        print(convidados)
    else:
        print('Operação finalizada!')
        break

