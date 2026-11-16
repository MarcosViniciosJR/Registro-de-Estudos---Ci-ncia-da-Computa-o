# Data: 26 de Maio de 2026
# Dupla: Marcos Vinicios e Eduarda  

lista = []
i = 0
while i < 2: # Criando a lista de quartos do Galinheiro
    num = int(input('Digite o número do codigo do quarto: '))
    tipo = input('Tipo de Acomodação (comum, premium ou luxo): ')
    preco = float(input('Preço da Diaria: '))
    disp = input('Digite a disponibilidade(s/n): ')
    lista.append([num, tipo, preco, disp])
    i = i + 1

i = 0
while i < len(lista): # Adicionando nos quartos se possui aquecimento
    lista[i].append(input('Digite se possui aquecimento de ovos (s/n): '))
    i = i + 1
print('\n')
soma = 0
i = 0

while i < len(lista): # Imprimindo as informações de cada quarto
    print('galinheiro:', i)
    print(lista[i])
    i = i + 1
print('Check-in\n')

i = 0
tem = 0
acom = input('tipo de acomodação desejada: ')
qt_dias = int(input('Quantidades de dias de pemanencia: '))
while i < len(lista) and tem == 0: # Fazendo o Check-in
    if acom == lista[i][1] and lista[i][3] == 's':
        lista[i][3] = 'Indisponivel'
        lista[i].append(qt_dias)
        valor = lista[i][2] * qt_dias
        tem = tem + 1
    i = i + 1
if tem > 0: # Verificando se possuiu vaga ou ñ
    print('Valor a ser pago: R$',valor)
else:
    print("Não possui quarto com a acomodação desejada!")

i = 0
while i < len(lista): # Imprimindo os quartos disponiveis restantes
    if lista[i][3] == 's':
        print('Numero do Espaço:',lista[i][0], '| tipo de acomodação:', lista[i][1], '| preço da diaria: R$', lista[i][2])
    i = i + 1
