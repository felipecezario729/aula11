from funcao5 import converter_metros_para_centimetro
from funcao6 import calcular_area_circulo
from funcao7 import calcular_area_quadrada

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
            calcular_area_circulo()
         elif opcao == '3':   
            calcular_area_quadrada()  
         elif opcao == '0':
              print(' Saindo do programa. Ate Logo !')
              break 
         else:
             print('Opão invalida - Tente novamente')

             
if __name__== "__main__":   
    menu()             
