#raw_input pega a informacao e o if compara para ver se e igual
user = raw_input('digite o nome do usuario: ')

if user == 'root':
    print 'Usuario logado como, %s' % user
#elfi adiciona mais uma comparacao
elif user == 'admin':
    print 'Usuario logado como, %s utilizando o elif' % user
#else e a saida    
else:
    print 'Usuario incorreto'
