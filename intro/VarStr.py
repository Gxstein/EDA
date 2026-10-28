a = 'paralelepipedo'  # Guarda a palavra na variável a

# FUNÇÕES DE STRING
maiuscula = a.upper()  # Converte tudo para maiúsculas
minuscula = a.lower()  # Converte tudo para minúsculas
capital = a.capitalize()  # Deixa a primeira letra maiúscula

print(minuscula)
print(maiuscula)
print(capital)

metade_da_palavra = a[0:7]  # Pega os índices de 0 até 6
ultimas_letras = a[7:]  # Pega do índice 7 até o final

print(metade_da_palavra)
print(ultimas_letras)

c = a.replace('lelepipedo', 'do')  # Substitui 'lelepipedo' por 'do'
print(c)

b = a.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0').replace('p', '9')  # Faz as substituições em sequência
print(b)

print(len(a))

d = a.strip()  # Remove espaços do início e do fim
print(d)

n1 = 14
n2 = 16

# F String

print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}')