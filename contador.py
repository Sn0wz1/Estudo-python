#Vai contar de 192.168.0.0 ate 192.168.0.255
'''
contador = 0
while contador <= 255:
    print '192.168.0.'+str(contador)
    contador = contador + 1
'''
#vai rodar ate acertar o usuario certo
'''
while True:
    user = raw_input('Digite o usuario: ')
    print 'O usuario digitado foi: %s' % user
    if user == 'root':
        print 'Usuario logado'
        break
'''
