'''
#for x in range, vai ler a lista 1~11
var = list()
for x in range(1,11):
#guarda os valores e quanto completar 10 imprime na tela
    var.append(raw_input('Digite um valor: '))
print var
'''

#while true vai rodar enquanto tiver valor raw_input vai pegar o valor enquanto
#for verdadeiro e armazenar no var.append, se o valor for negativo vai sai no
#else
var = list()
while True:
    msg = raw_input('Digite um valor ou nada para sair:')
    if msg:
        var.append(msg)
    else:
        break
#for valor in var: vai ler a lista exp [1][2][3][4]
#if valor == 'belo' comprar se o valor e belo,se tiver o valor belo ao sair print
# msg
'''
for valor in var:
    if valor == 'belo':
        print 'As musicas do belo sao muito ruins'
'''
