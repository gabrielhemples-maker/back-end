nome = str(input('digite seu nome completo')).strip()
dividido = nome.split()
print('seu 1° nome 2° é {}'.format(dividido[0]))
print('seu 1° nome 2° é {}'.format(dividido[len(dividido)-1]))
