vogais = 0

while True:

    palavra = input('Digite uma palavra (digite 1 para sair): ').lower()
    i = 0
    vogal = 'aeiou'
    if palavra == '1':
        break

    else:

        while i < len(palavra):
            letra = palavra[i]

            if letra == ' ':
                i += 1
                continue
            else:
                if letra in vogal:
                    vogais +=1
                i += 1
print(f'A quantidade de vogais é: {vogais}')
