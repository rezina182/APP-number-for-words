#Atividade 7, Avaliação Final-Python-22/06/2022
#Aluno:Renato do Nascimento Júnior, RA:226588

#Biblioteca utilizada para converter números em palavras
from num2words import num2words
#Input para receber o valor desejado
numero=input('Digite um valor em reais entre 0,01 e 999,99 somente números e a vírgula:')

if numero.find(',')!=-1:
#Comando para separar os valores que estão antes e depois da vírgula
    numero = numero.split(',')
#atribui a uma variavel e transforma em inteiro
    numero_p1 = int(numero[0])
    numero_p2 = int(numero[1])
else:
    numero_p1 = ''
    numero_p2 = ''    
#Condição para limitar o valor recebido,pode ser modular caso queira expandir os números acima de mil
if (numero_p1<=999 and numero_p1>=0 and numero_p2>=0 and numero_p2<=99 ):
    

#Condição caso o valor seja igual a 1 atribui 'real' senão atribui 'reais'
    if numero_p1 == 1:
        aux1 = ' real'
#Caso o valor antes da vírgula for '00' não escreve nada
    elif numero_p1==00:
        aux1=''
    else:
        aux1 = ' reais'
#Condição caso o valor seja igual a 1 atribui 'centavo' senão atribui 'centavos'       
    if numero_p2 == 1:
        aux2 = ' centavo'
#Caso o valor depois da vírgula for '00' não escreve nada
    elif numero_p2==00:
        aux2=''
    else:
        aux2 = ' centavos'
        
    text1 = ''
#Transforma os números em palavras e concatena com as variáveis aux1 e aux2
    text1 = num2words(numero_p1,lang='pt_BR') + str(aux1)
    text2 = num2words(numero_p2,lang='pt_BR') + str(aux2) 
#Caso o valor de text2 seja igual a 'zero' mostra somente o valor antes da vírgula
    if text2=='zero':
        print(text1)
#Caso o valor de text2 seja igual a 'zero' mostra somente o valor depois da vírgula
    elif text1=='zero':
        print(text2)
    else:
#Concatena os valores e atribui a uma variável
        resultado = text1 + ' e ' + text2
#Mostra na tela o valor recebido transformado em palavras
        print(resultado)
#Caso o valor digitado esteja fora dos limites mostra a mensagem informando
else:
    print("O valor digitado está fora dos limites estabelecidos!")
