# coding: utf-8

# print_textos.py

import sys


# Aqui eu converto do utf-8 para unicode e depois para latin1 ou cp850
# Se fizer direto, ele tentará usar a tabela ascii e dai...
texto = "Olá code page 1252!".decode("utf-8").encode('latin1')
texto2 = "Olá code page 850!".decode("utf-8").encode('cp850')

# Print comum
print texto
print texto2

print '--------------'

# Usando stdout
sys.stdout.write(texto + "\n")
sys.stdout.write(texto2 + "\n")
sys.stdout.flush()

sys.exit(0)
