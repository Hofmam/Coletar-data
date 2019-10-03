import pyautogui
import re

loop = 'Errei!'    # loop mantem o while

while loop == 'Errei!':
    data = pyautogui.prompt(text='informe a data da viagem com barras ( / ) e ano completo', title='Morretes à Curitiba', default='')
#aqui ^ pede a data da viagem, ao clicar em cacelar envia none pra variavel data

    if data != None:   #se data for diferente de none carac le quantos caracteres tem em data
        carac = len(data)
    if data == None:   #se data for none finaliza o Script
        exit()
    elif carac == 0:    #se o usuario não escrever nada da outro valor em data muda pra ser um erro
        data = '... será no dia éé ... Ué? ... Você deveria escrever uma data sabia!'
    elif carac != 10:   #se o numero de caracteres for diferente de 10 (carac) o data muda pra ser um erro
        data = '... Deveria ser 10 caracteres, parecido com 00/00/2019  com ( / ) e ano completo'
    elif not re.search('\d\d/\d\d/\d\d\d\d', data,):  #se  não encontar nesses 00/00/0000 (\d sao numeros)
        data = '... Você deve colocar a data com ( / ) entre o dia o mês e o ano tipo 00/00/2019'

    loop = pyautogui.confirm(text='a viagem vai ser no dia '+data, title='', buttons=['Ok', 'Errei!'])
#aqui ^ confirma com o usuario o valor de data e da um valor novo em loop (que mantem o while)

#nos proximos 3 if se verifica o valor de data e se estiver com algum dos erros listados  muda o loop para Errei!(para se manter em while)
    if data == '... será no dia éé ... Ué? ... Você deveria escrever uma data sabia!':
        loop = 'Errei!'
    if data == '... Deveria ser 10 caracteres, parecido com 00/00/2019  com ( / ) e ano completo':
        loop = 'Errei!'
    if data == '... Você deve colocar a data com ( / ) entre o dia o mês e o ano tipo 00/00/2019':
        loop = 'Errei!'
print(data)
