"""
exercicio 5:Faça um Programa que converta metros para centímetros.
exercicio 6:Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
exercicio 7:Faça um Programa que calcule a área de um quadrado,  em seguida mostre o dobro desta área para o usuário.
"""

def converter_metros_para_centimetro():
    metros = float(input('Metros: '))
    centimetros = metros * 100
    print(f'{metros} m = {centimetros} cm') 


def calcular_aera_circulo():
    raio = float(input('Informe o raio de um círculo: '))
    area = float((raio ** 2) * 3.14)  # (A = π r²) pi=3,1415
    print(f'Com um círculo de raio {raio} temos um círculo de área {area}.') 


def calcular_area_quadrada():
    lado = float(input('Informe  de um quadrado: '))        
    dobro = (lado**2) * 2                   
    area = lado**2  
    print(f'O dobro área do quadrado informado é de {dobro}')


def menu():
    while True: 
         print('\n --Menu de apções')
         print('1- converter metros para centimetros')
         print('2- calcular área do Circulo')
         print('3- calcular a área quadrada')
         print('0 - Sair')

         opcao = input('escolha uma opção') 
         if opcao == '1': 
            converter_metros_para_centimetro() 
         elif opcao == '2':   
            calcular_aera_circulo()
         elif opcao == '3':   
            calcular_area_quadrada()  
         elif opcao == '0':
              print(' Saindo do programa. Ate Logo !')
              break 
         else:
             print('Opão invalida - Tente novamente')

menu()             


