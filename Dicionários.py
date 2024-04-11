#1. Faça um programa que possua um Dicionário, adicione elementos ao dicionário e os mostre na tela.

Dicionario = {'Nome': 'Alex', 'Idade': 16, 'Altura': 1.74 }
print(Dicionario)

#2. Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos de mercado e seus respectivos preços e os mostre na tela.



i = 0

while i < 3:
  A = input("Insira um nome para o {}º produto: ".format(i+1))
  B = float(input("Insira o preço do {}: ".format(A)))
  Dicionario = {"produto": A, "preço": B}
  i = i + 1

print (Dicionario)





#3. Faça um programa, utilizando Dicionários, que peça para o usuário inserir quatro notas e mostre na tela as notas e a média entre elas.

notas = {}

for i in range (1, 5):
  nota = float(input(f"Insira a {i}° nota: "))
  notas[f"nota{i}"] = nota

media = sum(notas.values()) / len(notas)

print ("média: ", media)


#4. Faça um programa, utilizando Dicionários, que:

1° Passo: Peça para o usuário inserir quatro coisas em uma “Caixa Misteriosa” .

2° Passo: Peça para o usuário inserir um número.

3° Passo: Mostre na tela o que foi inserido na posição do número inserido pelo usuário.



Caixa_misteriosa = []

for i in range(4):
    item = input(f"Digite o {i+1}º item na Caixa Misteriosa: ")
    Caixa_misteriosa.append(item)

numero = int(input("Digite um número para revelar o que está na Caixa Misteriosa: "))

if 1 <= numero <= len(Caixa_misteriosa):
    print(f'O item na posição {numero} é: {Caixa_misteriosa[numero-1]}')
else:
    print("Número inválido.")


#5. Faça um programa, utilizando Dicionários, que:

1° Passo: Peça para o usuário inserir o nome de três funcionários e os mostre na tela.

2° Passo: Peça para o usuário demitir um funcionário e mostre na tela os funcionários restantes.

Funcionarios = {}

for i in range(3):
    Funcionario = input("Insira o nome do funcionário: ")
    Funcionarios[f'Funcionário{i+1}'] = Funcionario

print("Funcionários:", Funcionarios)

Demissao = input("Digite o nome do funcionário a ser demitido: ")

chaves_para_remover = [chave for chave, valor in Funcionarios.items() if valor == Demissao]

for chave in chaves_para_remover:
    del Funcionarios[chave]
    print(f'{Demissao} foi demitido.')

if not chaves_para_remover:
    print(f'{Demissao} não encontrado na lista de funcionários.')

print("Funcionários restantes:", Funcionarios)
