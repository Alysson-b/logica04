primeiro_numero = int(input('Digite o primeiro numero.'))
segundo_numero = int(input('Digite o segundo numero.'))

pares = 0

for num in range(primeiro_numero, segundo_numero + 1):
    if num % 2 == 0:
        pares += num

if pares > 0:
    print(f'A soma dos numeros pares no intervalo de {primeiro_numero} a {segundo_numero} é {pares}')
else:
    print(f'Nao ha numeros pares no intervalo de {primeiro_numero} a {segundo_numero}.')