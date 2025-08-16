def calcular_media_notas():
    notas = []
    for i in range(1, 5):
        nota = float(input(f'Digite a {i}ª Bimestral'))
        notas.append(nota)
    media = sum(notas)/ len(notas)
    print(f' A media das notas informadas é {media:.2f}')

# chamada de função
calcular_media_notas()

# n1 = float( input('digite um número para somar'))
# n2 = float(input('digite outro número')) 
# n3 = float(input('digite um outra nota'))
# n4 = float(input('digite uma outra nota'))
# media = (n1+n2+n3+n4)/4
# print( f' a  media das notas informada é')

