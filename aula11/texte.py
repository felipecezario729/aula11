
def notas_medias_alunos():


    nmaior7 = soma =  0
    vetormedia = []
# range 3 é o total de alunos
    for i in range(3):# para não criar um teste longo coloque 3
    # faixa de notas ==> 4 [0,1,2,3]

        for j in range(4):
            nota =  float(input(f'Digite a {j+1}º nota do {i+1}º Aluno'))
            soma = soma + nota
            media = soma / 4
            soma = 0
        vetormedia.append(media)
        print ('----')
    for i in range(3):
        if vetormedia[i] >=7:
            nmaior7 = nmaior7 +1
        print(f'A quantidade de aluno que teve a nota maior ou igual a 7 foi {nmaior7}')

notas_medias_alunos()

