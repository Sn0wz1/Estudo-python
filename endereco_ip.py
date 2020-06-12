#raw_input pega a informacao digitada
ip = raw_input('Digite um endereco IP: ')
print 'O endereco ' + ip + ' e um endereco valido!'
#%s ao inves de usar + ip +
print 'O endereco %s e um endereco valido!' % ip
#len faz a conta de quantos numeros
print 'O endereco %s tem o tamanho de %s caracteres' %(ip,str(len(ip)))
#%f mostra um numero quebrado exp 1.245552
print 'numero quebrado %f' % 1.245555
#%.2f mostra apenas 2 caracteres exp 1.25
print 'numero quebrado %.2f' % 1.24555
